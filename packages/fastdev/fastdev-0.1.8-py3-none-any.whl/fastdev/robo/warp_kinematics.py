# mypy: disable-error-code="valid-type"
from typing import TYPE_CHECKING, Optional, Tuple

import numpy as np
import torch
import warp as wp
from jaxtyping import Float

if TYPE_CHECKING:
    from fastdev.robo.robot_model import RobotModel


@wp.func
def axis_angle_to_tf_mat(axis: wp.vec3, angle: wp.float32):
    x, y, z = axis[0], axis[1], axis[2]
    s, c = wp.sin(angle), wp.cos(angle)
    C = 1.0 - c

    xs, ys, zs = x * s, y * s, z * s
    xC, yC, zC = x * C, y * C, z * C
    xyC, yzC, zxC = x * yC, y * zC, z * xC

    # fmt: off
    return wp.mat44(
        x * xC + c, xyC - zs, zxC + ys, 0.0,
        xyC + zs, y * yC + c, yzC - xs, 0.0,
        zxC - ys, yzC + xs, z * zC + c, 0.0,
        0.0, 0.0, 0.0, 1.0,
    )
    # fmt: on


@wp.func
def axis_distance_to_tf_mat(axis: wp.vec3, distance: wp.float32):
    x, y, z = axis[0], axis[1], axis[2]
    # fmt: off
    return wp.mat44(
        1.0, 0.0, 0.0, distance * x,
        0.0, 1.0, 0.0, distance * y,
        0.0, 0.0, 1.0, distance * z,
        0.0, 0.0, 0.0, 1.0,
    )
    # fmt: on


@wp.kernel
def forward_kinematics_kernel(
    joint_values: wp.array2d(dtype=wp.float32),  # [b, num_dofs]
    link_indices_topological_order: wp.array(dtype=wp.int32),
    link_joint_types: wp.array(dtype=wp.int32),
    link_joint_indices: wp.array(dtype=wp.int32),
    link_joint_origins: wp.array(dtype=wp.mat44),
    parent_link_indices: wp.array(dtype=wp.int32),
    joint_axes: wp.array(dtype=wp.vec3),
    link_poses: wp.array2d(dtype=wp.mat44),  # output, [b, num_links]
):
    b_idx = wp.tid()
    for link_index in range(link_indices_topological_order.shape[0]):
        joint_type = link_joint_types[link_index]
        if joint_type == -1:
            glb_joint_pose = wp.identity(n=4, dtype=wp.float32)  # type: ignore
        else:
            parent_link_index = parent_link_indices[link_index]
            parent_link_pose = link_poses[b_idx, parent_link_index]
            joint_index = link_joint_indices[link_index]
            if joint_type == 0:
                local_joint_tf = wp.identity(n=4, dtype=wp.float32)  # type: ignore
            elif joint_type == 1:  # prismatic
                joint_value = joint_values[b_idx, joint_index]
                joint_axis = joint_axes[joint_index]
                local_joint_tf = axis_distance_to_tf_mat(joint_axis, joint_value)
            elif joint_type == 2:  # revolute
                joint_value = joint_values[b_idx, joint_index]
                joint_axis = joint_axes[joint_index]
                local_joint_tf = axis_angle_to_tf_mat(joint_axis, joint_value)
            joint_origin = link_joint_origins[link_index]
            glb_joint_pose = (parent_link_pose @ joint_origin) @ local_joint_tf  # type: ignore
        link_poses[b_idx, link_index] = glb_joint_pose


class ForwardKinematics(torch.autograd.Function):
    @staticmethod
    def forward(
        ctx, joint_values: Float[torch.Tensor, "*b num_dofs"], robot_model: "RobotModel"
    ) -> Float[torch.Tensor, "*b num_links 4 4"]:
        num_dofs = joint_values.shape[-1]
        num_links = len(robot_model.link_names)

        joint_values_wp = wp.from_torch(
            joint_values.contiguous().view(-1, num_dofs), dtype=wp.float32, requires_grad=joint_values.requires_grad
        )
        link_poses_wp = wp.from_torch(
            torch.zeros(
                (joint_values_wp.shape[0], num_links, 4, 4),
                device=joint_values.device,
                dtype=joint_values.dtype,
                requires_grad=joint_values.requires_grad,
            ),
            dtype=wp.mat44,
            requires_grad=joint_values.requires_grad,
        )
        link_indices_topological_order = wp.from_torch(
            robot_model.link_indices_topological_order.contiguous(), dtype=wp.int32
        )
        link_joint_types = wp.from_torch(robot_model.link_joint_types.contiguous(), dtype=wp.int32)
        link_joint_indices = wp.from_torch(robot_model.link_joint_indices.contiguous(), dtype=wp.int32)
        link_joint_origins = wp.from_torch(robot_model.link_joint_origins.contiguous(), dtype=wp.mat44)
        parent_link_indices = wp.from_torch(robot_model.parent_link_indices.contiguous(), dtype=wp.int32)
        joint_axes = wp.from_torch(robot_model.joint_axes.contiguous(), dtype=wp.vec3)

        wp.launch(
            kernel=forward_kinematics_kernel,
            dim=(joint_values_wp.shape[0],),
            inputs=[
                joint_values_wp,
                link_indices_topological_order,
                link_joint_types,
                link_joint_indices,
                link_joint_origins,
                parent_link_indices,
                joint_axes,
            ],
            outputs=[link_poses_wp],
            device=joint_values_wp.device,
        )

        if joint_values.requires_grad:
            ctx.joint_values_wp = joint_values_wp
            ctx.link_poses_wp = link_poses_wp
            ctx.num_dofs = num_dofs
            ctx.num_links = num_links
            ctx.link_indices_topological_order = link_indices_topological_order
            ctx.link_joint_types = link_joint_types
            ctx.link_joint_indices = link_joint_indices
            ctx.link_joint_origins = link_joint_origins
            ctx.parent_link_indices = parent_link_indices
            ctx.joint_axes = joint_axes

        return wp.to_torch(link_poses_wp).view(joint_values.shape[:-1] + (num_links, 4, 4))

    @staticmethod
    def backward(  # type: ignore
        ctx, link_poses_grad: Float[torch.Tensor, "*b num_links 4 4"]
    ) -> Tuple[Optional[Float[torch.Tensor, "*b num_dofs"]], None]:  # noqa: F821
        if ctx.joint_values_wp.requires_grad:
            ctx.link_poses_wp.grad = wp.from_torch(
                link_poses_grad.contiguous().view(-1, ctx.num_links, 4, 4), dtype=wp.mat44
            )
            wp.launch(
                kernel=forward_kinematics_kernel,
                dim=(ctx.joint_values_wp.shape[0],),
                inputs=[
                    ctx.joint_values_wp,
                    ctx.link_indices_topological_order,
                    ctx.link_joint_types,
                    ctx.link_joint_indices,
                    ctx.link_joint_origins,
                    ctx.parent_link_indices,
                    ctx.joint_axes,
                ],
                outputs=[ctx.link_poses_wp],
                adj_inputs=[ctx.joint_values_wp.grad, None, None, None, None, None, None],
                adj_outputs=[ctx.link_poses_wp.grad],
                adjoint=True,
                device=ctx.joint_values_wp.device,
            )
            joint_values_grad = wp.to_torch(ctx.joint_values_wp.grad).view(link_poses_grad.shape[:-3] + (ctx.num_dofs,))
        else:
            joint_values_grad = None
        return joint_values_grad, None


def forward_kinematics(
    joint_values: Float[torch.Tensor, "*b num_dofs"],  # noqa: F821
    robot_model: "RobotModel",
) -> Float[torch.Tensor, "*b num_links 4 4"]:
    return ForwardKinematics.apply(joint_values, robot_model)  # type: ignore


def forward_kinematics_numpy(
    joint_values: Float[np.ndarray, "*b num_dofs"],  # noqa: F821
    robot_model: "RobotModel",
) -> Float[np.ndarray, "*b num_links 4 4"]:
    num_dofs = joint_values.shape[-1]
    num_links = len(robot_model.link_names)

    joint_values_wp = wp.from_numpy(joint_values.reshape(-1, num_dofs), dtype=wp.float32)  # [B, num_dofs]
    link_poses_wp = wp.from_numpy(
        np.zeros(
            (joint_values_wp.shape[0], num_links, 4, 4),
            dtype=joint_values.dtype,
        ),
        dtype=wp.mat44,
    )
    link_indices_topological_order = wp.from_numpy(robot_model.get_link_indices_topological_order("np"), dtype=wp.int32)
    link_joint_types = wp.from_numpy(robot_model.get_link_joint_types("np"), dtype=wp.int32)
    link_joint_indices = wp.from_numpy(robot_model.get_link_joint_indices("np"), dtype=wp.int32)
    link_joint_origins = wp.from_numpy(robot_model.get_link_joint_origins("np"), dtype=wp.mat44)
    parent_link_indices = wp.from_numpy(robot_model.get_parent_link_indices("np"), dtype=wp.int32)
    joint_axes = wp.from_numpy(robot_model.get_joint_axes("np"), dtype=wp.vec3)

    wp.launch(
        kernel=forward_kinematics_kernel,
        dim=(joint_values_wp.shape[0],),
        inputs=[
            joint_values_wp,
            link_indices_topological_order,
            link_joint_types,
            link_joint_indices,
            link_joint_origins,
            parent_link_indices,
            joint_axes,
        ],
        outputs=[link_poses_wp],
        device=joint_values_wp.device,
    )

    return link_poses_wp.numpy().reshape(joint_values.shape[:-1] + (num_links, 4, 4))
