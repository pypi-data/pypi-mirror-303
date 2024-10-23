# mypy: disable-error-code="valid-type"
from typing import Dict, Literal, Optional, Tuple, get_args

import numpy as np
import torch
import warp as wp
from beartype import beartype
from jaxtyping import Float


@wp.kernel
def axis_angle_to_matrix_via_quat_kernel(
    axis: wp.array(dtype=wp.vec3),
    angle: wp.array(dtype=wp.float32),
    rot_mat: wp.array(dtype=wp.mat33),
):
    tid = wp.tid()
    rot_mat[tid] = wp.quat_to_matrix(wp.quat_from_axis_angle(axis[tid], angle[tid]))


@wp.kernel
def axis_angle_to_matrix_kernel(
    axis: wp.array(dtype=wp.vec3),
    angle: wp.array(dtype=wp.float32),
    rot_mat: wp.array(dtype=wp.mat33),
):
    tid = wp.tid()

    axis_elem = axis[tid]
    x, y, z = axis_elem[0], axis_elem[1], axis_elem[2]
    s, c = wp.sin(angle[tid]), wp.cos(angle[tid])
    C = 1.0 - c

    xs, ys, zs = x * s, y * s, z * s
    xC, yC, zC = x * C, y * C, z * C
    xyC, yzC, zxC = x * yC, y * zC, z * xC

    rot_mat[tid] = wp.mat33(
        x * xC + c, xyC - zs, zxC + ys, xyC + zs, y * yC + c, yzC - xs, zxC - ys, yzC + xs, z * zC + c
    )


class AxisAngleToMatrix(torch.autograd.Function):
    @staticmethod
    def forward(
        ctx, axis: Float[torch.Tensor, "... 3"], angle: Float[torch.Tensor, "..."]
    ) -> Float[torch.Tensor, "... 3 3"]:
        axis_wp = wp.from_torch(axis.view(-1, 3), dtype=wp.vec3, requires_grad=axis.requires_grad)
        angles_wp = wp.from_torch(angle.view(-1), dtype=wp.float32, requires_grad=angle.requires_grad)
        rot_mat_wp = wp.empty(
            axis_wp.shape,
            dtype=wp.mat33,  # type: ignore
            device=axis_wp.device,
            requires_grad=axis_wp.requires_grad or angles_wp.requires_grad,
        )
        wp.launch(
            kernel=axis_angle_to_matrix_kernel,
            dim=(axis_wp.shape[0],),
            inputs=[axis_wp, angles_wp],
            outputs=[rot_mat_wp],
            device=axis_wp.device,
        )
        if axis.requires_grad or angle.requires_grad:
            ctx.axis_wp = axis_wp
            ctx.angles_wp = angles_wp
            ctx.rot_mat_wp = rot_mat_wp
        return wp.to_torch(rot_mat_wp).view(angle.shape + (3, 3))

    @staticmethod
    def backward(  # type: ignore
        ctx, rot_mat_grad: Float[torch.Tensor, "... 3 3"]
    ) -> Tuple[Optional[Float[torch.Tensor, "... 3"]], Optional[Float[torch.Tensor, "..."]]]:
        ctx.rot_mat_wp.grad = wp.from_torch(rot_mat_grad.contiguous().view(-1, 3, 3), dtype=wp.mat33)
        wp.launch(
            kernel=axis_angle_to_matrix_kernel,
            dim=(ctx.axis_wp.shape[0],),
            inputs=[ctx.axis_wp, ctx.angles_wp],
            outputs=[ctx.rot_mat_wp],
            adj_inputs=[ctx.axis_wp.grad, ctx.angles_wp.grad],
            adj_outputs=[ctx.rot_mat_wp.grad],
            adjoint=True,
            device=ctx.axis_wp.device,
        )
        axis_grad = wp.to_torch(ctx.axis_wp.grad).view(rot_mat_grad.shape[:-1]) if ctx.axis_wp.requires_grad else None
        angle_grad = (
            wp.to_torch(ctx.angles_wp.grad).view(rot_mat_grad.shape[:-2]) if ctx.angles_wp.requires_grad else None
        )
        return axis_grad, angle_grad


@beartype
def axis_angle_to_matrix(
    axis: Float[torch.Tensor, "... 3"], angle: Float[torch.Tensor, "..."]
) -> Float[torch.Tensor, "... 3 3"]:
    """
    Converts axis angles to rotation matrices using Rodrigues formula.

    Args:
        axis (torch.Tensor): axis, the shape could be [..., 3].
        angle (torch.Tensor): angle, the shape could be [...].

    Returns:
        torch.Tensor: Rotation matrices [..., 3, 3].

    Example:
        >>> axis = torch.tensor([1.0, 0.0, 0.0])
        >>> angle = torch.tensor(0.5)
        >>> axis_angle_to_matrix(axis, angle)
        tensor([[ 1.0000,  0.0000,  0.0000],
                [ 0.0000,  0.8776, -0.4794],
                [ 0.0000,  0.4794,  0.8776]])
    """
    return AxisAngleToMatrix.apply(axis, angle)  # type: ignore


# fmt: off
_AXES = Literal[
    "sxyz", "sxyx", "sxzy", "sxzx", "syzx", "syzy", "syxz", "syxy", "szxy", "szxz", "szyx", "szyz",
    "rzyx", "rxyx", "ryzx", "rxzx", "rxzy", "ryzy", "rzxy", "ryxy", "ryxz", "rzxz", "rxyz", "rzyz"
]
# fmt: on
_AXES_SPEC: Dict[_AXES, wp.vec4i] = {
    axes: wp.vec4i("sr".index(axes[0]), "xyz".index(axes[1]), "xyz".index(axes[2]), "xyz".index(axes[3]))
    for axes in get_args(_AXES)
}


@wp.func
def _euler_angle_to_matrix(angle: wp.float32, axis: wp.int32) -> wp.mat33:
    c, s = wp.cos(angle), wp.sin(angle)
    if axis == 0:
        return wp.mat33(1.0, 0.0, 0.0, 0.0, c, -s, 0.0, s, c)
    elif axis == 1:
        return wp.mat33(c, 0.0, s, 0.0, 1.0, 0.0, -s, 0.0, c)
    else:
        return wp.mat33(c, -s, 0.0, s, c, 0.0, 0.0, 0.0, 1.0)


@wp.kernel
def euler_angles_to_matrix_kernel(
    euler_angles: wp.array(dtype=wp.vec3), axes: wp.vec4i, rot_mat: wp.array(dtype=wp.mat33)
):
    tid = wp.tid()
    euler_angles_elem = euler_angles[tid]

    if axes[0] == 0:  # static/extrinsic rotation
        rot_mat[tid] = wp.mul(
            wp.mul(
                _euler_angle_to_matrix(euler_angles_elem[2], axes[3]),
                _euler_angle_to_matrix(euler_angles_elem[1], axes[2]),
            ),
            _euler_angle_to_matrix(euler_angles_elem[0], axes[1]),
        )
    else:  # rotating/intrinsic rotation
        rot_mat[tid] = wp.mul(
            wp.mul(
                _euler_angle_to_matrix(euler_angles_elem[0], axes[1]),
                _euler_angle_to_matrix(euler_angles_elem[1], axes[2]),
            ),
            _euler_angle_to_matrix(euler_angles_elem[2], axes[3]),
        )


class EulerAnglesToMatrix(torch.autograd.Function):
    @staticmethod
    def forward(
        ctx, euler_angles: Float[torch.Tensor, "... 3"], axes: _AXES = "sxyz"
    ) -> Float[torch.Tensor, "... 3 3"]:
        axes = axes.lower()  # type: ignore
        if len(axes) == 3:
            axes = f"s{axes}"  # type: ignore
        if axes not in _AXES_SPEC:
            raise ValueError(f"Invalid axes: {axes}")

        euler_angles_wp = wp.from_torch(
            euler_angles.view(-1, 3).contiguous(), dtype=wp.vec3, requires_grad=euler_angles.requires_grad
        )
        rot_mat_wp = wp.from_torch(
            torch.empty(
                euler_angles.shape + (3,),
                dtype=euler_angles.dtype,
                device=euler_angles.device,
                requires_grad=euler_angles.requires_grad,
            ).view(-1, 3, 3),
            dtype=wp.mat33,
            requires_grad=euler_angles.requires_grad,
        )
        axes_spec = _AXES_SPEC[axes]

        wp.launch(
            kernel=euler_angles_to_matrix_kernel,
            dim=(euler_angles_wp.shape[0],),
            inputs=[euler_angles_wp, axes_spec],
            outputs=[rot_mat_wp],
            device=euler_angles_wp.device,
        )
        if euler_angles.requires_grad:
            ctx.euler_angles_wp = euler_angles_wp
            ctx.rot_mat_wp = rot_mat_wp
            ctx.axes_spec = axes_spec
        return wp.to_torch(rot_mat_wp).view(euler_angles.shape + (3,))

    @staticmethod
    def backward(  # type: ignore
        ctx, rot_mat_grad: Float[torch.Tensor, "... 3 3"]
    ) -> Tuple[Optional[Float[torch.Tensor, "... 3"]], None]:
        ctx.rot_mat_wp.grad = wp.from_torch(rot_mat_grad.contiguous().view(-1, 3, 3), dtype=wp.mat33)
        wp.launch(
            kernel=euler_angles_to_matrix_kernel,
            dim=(ctx.euler_angles_wp.shape[0],),
            inputs=[ctx.euler_angles_wp, ctx.axes_spec],
            outputs=[ctx.rot_mat_wp],
            adj_inputs=[ctx.euler_angles_wp.grad, ctx.axes_spec],
            adj_outputs=[ctx.rot_mat_wp.grad],
            adjoint=True,
            device=ctx.euler_angles_wp.device,
        )
        return wp.to_torch(ctx.euler_angles_wp.grad).view(rot_mat_grad.shape[:-1]), None


@beartype
def euler_angles_to_matrix(
    euler_angles: Float[torch.Tensor, "... 3"], axes: _AXES = "sxyz"
) -> Float[torch.Tensor, "... 3 3"]:
    """Converts Euler angles to rotation matrices.

    Args:
        euler_angles (torch.Tensor): Tensor of Euler angles with shape [..., 3].
        axes (str): Axis specification string, one of 24 possible sequences (e.g., "sxyz"). If only 3 characters are provided, "s" will be prefixed.

    Returns:
        torch.Tensor: Rotation matrices with shape [..., 3, 3].

    Example:
        >>> euler_angles = torch.tensor([1.0, 0.5, 2.0])
        >>> euler_angles_to_matrix(euler_angles, axes="sxyz")
        tensor([[-0.3652, -0.6592,  0.6574],
                [ 0.7980,  0.1420,  0.5857],
                [-0.4794,  0.7385,  0.4742]])
        >>> euler_angles_to_matrix(euler_angles, axes="rxyz")
        tensor([[-0.3652, -0.7980,  0.4794],
                [ 0.3234, -0.5917, -0.7385],
                [ 0.8729, -0.1146,  0.4742]])
    """
    return EulerAnglesToMatrix.apply(euler_angles, axes)  # type: ignore


@wp.kernel
def matrix_to_quaternion_kernel(
    rot_mat: wp.array(dtype=wp.mat33),
    scalar_first: bool,
    canonical: bool,
    quat: wp.array(dtype=wp.quat),
):
    tid = wp.tid()
    q = wp.quat_from_matrix(rot_mat[tid])  # warp assumes scalar last, xyzw
    if canonical:
        if q[3] < 0:
            q = wp.quat(-q[0], -q[1], -q[2], -q[3])
    if scalar_first:
        q = wp.quat(q[3], q[0], q[1], q[2])  # xyzw -> wxyz
    quat[tid] = q


class MatrixToQuaternion(torch.autograd.Function):
    @staticmethod
    def forward(
        ctx, rot_mat: Float[torch.Tensor, "... 3 3"], scalar_first: bool = True, canonical: bool = True
    ) -> Float[torch.Tensor, "... 4"]:
        rot_mat_wp = wp.from_torch(
            rot_mat.contiguous().view(-1, 3, 3), dtype=wp.mat33, requires_grad=rot_mat.requires_grad
        )
        quat_wp = wp.from_torch(
            torch.empty(
                rot_mat.shape[:-2] + (4,),
                dtype=rot_mat.dtype,
                device=rot_mat.device,
                requires_grad=rot_mat.requires_grad,
            ).view(-1, 4),
            dtype=wp.quat,
            requires_grad=rot_mat.requires_grad,
        )
        wp.launch(
            kernel=matrix_to_quaternion_kernel,
            dim=(rot_mat_wp.shape[0],),
            inputs=[rot_mat_wp, scalar_first, canonical],
            outputs=[quat_wp],
            device=rot_mat_wp.device,
        )
        if rot_mat.requires_grad:
            ctx.scalar_first = scalar_first
            ctx.canonical = canonical
            ctx.rot_mat_wp = rot_mat_wp
            ctx.quat_wp = quat_wp
        return wp.to_torch(quat_wp).view(rot_mat.shape[:-2] + (4,))

    @staticmethod
    def backward(  # type: ignore
        ctx, quat_grad: Float[torch.Tensor, "... 4"]
    ) -> Tuple[Optional[Float[torch.Tensor, "... 3 3"]], None, None]:
        ctx.quat_wp.grad = wp.from_torch(quat_grad.contiguous().view(-1, 4), dtype=wp.quat)
        wp.launch(
            kernel=matrix_to_quaternion_kernel,
            dim=(ctx.rot_mat_wp.shape[0],),
            inputs=[ctx.rot_mat_wp, ctx.scalar_first, ctx.canonical],
            outputs=[ctx.quat_wp],
            adj_inputs=[ctx.rot_mat_wp.grad, ctx.scalar_first, ctx.canonical],
            adj_outputs=[ctx.quat_wp.grad],
            adjoint=True,
            device=ctx.rot_mat_wp.device,
        )
        return wp.to_torch(ctx.rot_mat_wp.grad).view(quat_grad.shape[:-1] + (3, 3)), None, None


@beartype
def matrix_to_quaternion(
    rot_mat: Float[torch.Tensor, "... 3 3"], scalar_first: bool = True, canonical: bool = True
) -> Float[torch.Tensor, "... 4"]:
    """
    Converts rotation matrices to quaternions.

    Args:
        rot_mat (torch.Tensor): Rotation matrices with shape [..., 3, 3].

    Returns:
        torch.Tensor: Quaternions with shape [..., 4].

    Example:
        >>> rot_mat = torch.tensor([[-0.2533, -0.6075,  0.7529],
        ...                         [ 0.8445, -0.5185, -0.1343],
        ...                         [ 0.4720,  0.6017,  0.6443]])
        >>> matrix_to_quaternion(rot_mat)
        tensor([0.4671, 0.3940, 0.1503, 0.7772])

    .. note::
        The gradient of this function differs from the pytorch3d implementation, but it
        should be okay for most use cases. Ref_

    .. _Ref: https://github.com/facebookresearch/pytorch3d/issues/503#issuecomment-755493515
    """
    return MatrixToQuaternion.apply(rot_mat, scalar_first, canonical)


@beartype
def matrix_to_quaternion_numpy(
    rot_mat: Float[np.ndarray, "... 3 3"], scalar_first: bool = True, canonical: bool = True
) -> Float[np.ndarray, "... 4"]:
    """
    Converts rotation matrices to quaternions.

    Args:
        rot_mat (np.ndarray): Rotation matrices with shape [..., 3, 3].

    Returns:
        np.ndarray: Quaternions with shape [..., 4].

    Example:
        >>> rot_mat = np.array([[ 0.45930517, -0.11985919, -0.88015485],
        ...                     [-0.4041326 ,  0.85417026, -0.32721555],
        ...                     [ 0.7910219 ,  0.50599104,  0.3438858 ]])
        >>> matrix_to_quaternion_numpy(rot_mat)
        array([ 0.8150708 ,  0.25556272, -0.5125865 , -0.08719288], dtype=float32)

    """
    rot_mat_wp = wp.from_numpy(rot_mat.reshape((-1, 3, 3)), dtype=wp.mat33)
    quat_wp = wp.from_numpy(np.empty(rot_mat.shape[:-2] + (4,), dtype=rot_mat.dtype).reshape((-1, 4)), dtype=wp.quat)
    wp.launch(
        kernel=matrix_to_quaternion_kernel,
        dim=(rot_mat_wp.shape[0],),
        inputs=[rot_mat_wp, scalar_first, canonical],
        outputs=[quat_wp],
        device=rot_mat_wp.device,
    )
    return quat_wp.numpy().reshape(rot_mat.shape[:-2] + (4,))


__all__ = ["axis_angle_to_matrix", "euler_angles_to_matrix", "matrix_to_quaternion", "matrix_to_quaternion_numpy"]
