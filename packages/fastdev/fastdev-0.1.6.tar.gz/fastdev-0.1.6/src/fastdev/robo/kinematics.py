from typing import TYPE_CHECKING

import torch
from jaxtyping import Float

from fastdev.xform.rotation import axis_angle_to_matrix  # warp's version may don't support broadcasting, use this
from fastdev.xform.transforms import rot_tl_to_tf_mat

if TYPE_CHECKING:
    from fastdev.robo.robot_model import RobotModel


def forward_kinematics(
    joint_values: Float[torch.Tensor, "b num_dofs"], robot_model: "RobotModel"
) -> Float[torch.Tensor, "b num_links 4 4"]:
    pris_jnt_tf = rot_tl_to_tf_mat(tl=robot_model.joint_axes * joint_values.unsqueeze(-1))
    rev_jnt_tf = rot_tl_to_tf_mat(rot_mat=axis_angle_to_matrix(robot_model.joint_axes, joint_values))

    num_links = robot_model.link_indices_topological_order.shape[0]
    link_poses = torch.eye(4).to(joint_values).repeat(joint_values.shape[:-1] + (num_links, 1, 1))

    for link_index in robot_model.link_indices_topological_order:
        joint_type = robot_model.link_joint_types[link_index]
        if (joint_type == -1).item():
            continue
        else:
            parent_link_pose = link_poses[:, robot_model.parent_link_indices[link_index]]
            joint_index = robot_model.link_joint_indices[link_index]
            if (joint_type == 1).item():
                local_joint_tf = pris_jnt_tf[:, joint_index]
            elif (joint_type == 2).item():
                local_joint_tf = rev_jnt_tf[:, joint_index]
            else:  # joint_type == 0
                local_joint_tf = torch.eye(4).to(joint_values).expand(joint_values.shape[:-1] + (4, 4))
            joint_origin = robot_model.link_joint_origins[link_index]
            glb_joint_pose = (parent_link_pose @ joint_origin) @ local_joint_tf
            link_poses[:, link_index] = glb_joint_pose
    return link_poses
