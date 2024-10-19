"""
1. Fix a tensor contiguous issue in curobo 0.7.4
2. Speed up CudaRobotGenerator with a large number of spheres without collision checking

Maybe consider submitting a PR to curobo to fix the issue.
"""

from typing import Tuple

import torch
from curobo.cuda_robot_model.cuda_robot_generator import CudaRobotGenerator, CudaRobotGeneratorConfig
from curobo.cuda_robot_model.cuda_robot_model import CudaRobotModel, CudaRobotModelConfig
from curobo.curobolib.kinematics import KinematicsFusedFunction
from curobo.util.logger import log_error, log_info, log_warn
from torch import Tensor


class CustomKinematicsFusedFunction(KinematicsFusedFunction):
    @staticmethod
    def backward(ctx, grad_out_link_pos, grad_out_link_quat, grad_out_spheres):
        return KinematicsFusedFunction.backward(
            ctx,
            grad_out_link_pos.contiguous(),  # NOTE a fix here
            grad_out_link_quat.contiguous(),  # NOTE a fix here
            grad_out_spheres,
        )


def custom_get_cuda_kinematics(
    link_pos_seq,
    link_quat_seq,
    batch_robot_spheres,
    global_cumul_mat,
    q_in,
    fixed_transform,
    link_spheres_tensor,
    link_map,  # tells which link is attached to which link i
    joint_map,  # tells which joint is attached to a link i
    joint_map_type,  # joint type
    store_link_map,
    link_sphere_idx_map,  # sphere idx map
    link_chain_map,
    joint_offset_map,
    grad_out_q,
    use_global_cumul: bool = True,
):
    # if not q_in.is_contiguous():
    #    q_in = q_in.contiguous()
    link_pos, link_quat, robot_spheres = CustomKinematicsFusedFunction.apply(  # type: ignore
        link_pos_seq,
        link_quat_seq,
        batch_robot_spheres,
        global_cumul_mat,
        q_in,
        fixed_transform,
        link_spheres_tensor,
        link_map,  # tells which link is attached to which link i
        joint_map,  # tells which joint is attached to a link i
        joint_map_type,  # joint type
        store_link_map,
        link_sphere_idx_map,  # sphere idx map
        link_chain_map,
        joint_offset_map,
        grad_out_q,
        use_global_cumul,
    )
    return link_pos, link_quat, robot_spheres


class CustomCudaRobotGenerator(CudaRobotGenerator):
    def _create_self_collision_thread_data(  # type: ignore
        self, collision_threshold: torch.Tensor
    ) -> Tuple[torch.Tensor, int, bool, int]:
        """Create thread data for self collision checks.

        Args:
            collision_threshold: Collision distance between spheres of the robot. Used to
                skip self collision checks when distance is -inf.

        Returns:
            Tuple[torch.Tensor, int, bool, int]: Thread location for self collision checks,
                number of self collision checks, if thread calculation was successful,
                and number of checks per thread.

        """
        coll_cpu = collision_threshold.cpu()
        max_checks_per_thread = 512
        thread_loc = torch.zeros((2 * 32 * max_checks_per_thread), dtype=torch.int16) - 1
        n_spheres = coll_cpu.shape[0]
        sl_idx = 0
        skip_count = 0
        all_val = 0
        valid_data = True
        for i in range(n_spheres):
            if not valid_data:
                break
            if torch.max(coll_cpu[i]) == -torch.inf:
                log_info("skip" + str(i))
                skip_count += n_spheres - i
                all_val += n_spheres - i
                continue  # NOTE a speed up here
            for j in range(i + 1, n_spheres):
                if sl_idx > thread_loc.shape[0] - 1:
                    valid_data = False
                    log_warn(
                        "Self Collision checks are greater than "
                        + str(32 * max_checks_per_thread)
                        + ", using slower kernel"
                    )
                    break
                if coll_cpu[i, j] != -torch.inf:
                    thread_loc[sl_idx] = i
                    sl_idx += 1
                    thread_loc[sl_idx] = j
                    sl_idx += 1
                else:
                    skip_count += 1
                all_val += 1
        log_info("Self Collision threads, skipped %: " + str(100 * float(skip_count) / all_val))
        log_info("Self Collision count: " + str(sl_idx / (2)))
        log_info("Self Collision per thread: " + str(sl_idx / (2 * 1024)))

        max_checks_per_thread = 512
        val = sl_idx / (2 * 1024)
        if val < 1:
            max_checks_per_thread = 1
        elif val < 2:
            max_checks_per_thread = 2
        elif val < 4:
            max_checks_per_thread = 4
        elif val < 8:
            max_checks_per_thread = 8
        elif val < 32:
            max_checks_per_thread = 32
        elif val < 64:
            max_checks_per_thread = 64
        elif val < 128:
            max_checks_per_thread = 128
        elif val < 512:
            max_checks_per_thread = 512
        else:
            log_error(
                "Self Collision not supported as checks are greater than 32 * 512, \
                      reduce number of spheres used to approximate the robot."
            )

        if max_checks_per_thread < 2:
            max_checks_per_thread = 2
        log_info("Self Collision using: " + str(max_checks_per_thread))

        return (
            thread_loc.to(device=collision_threshold.device),
            sl_idx,
            valid_data,
            max_checks_per_thread,
        )


class CustomCudaRobotModelConfig(CudaRobotModelConfig):
    @staticmethod
    def from_config(config: CudaRobotGeneratorConfig) -> CudaRobotModelConfig:
        """Create a robot model configuration from a generator configuration.

        Args:
            config: Input robot generator configuration.

        Returns:
            CudaRobotModelConfig: robot model configuration.
        """
        # create a config generator and load all values
        generator = CustomCudaRobotGenerator(config)
        return CudaRobotModelConfig(
            tensor_args=generator.tensor_args,
            link_names=generator.link_names,  # type: ignore
            kinematics_config=generator.kinematics_config,
            self_collision_config=generator.self_collision_config,
            kinematics_parser=generator.kinematics_parser,
            use_global_cumul=generator.use_global_cumul,
            compute_jacobian=generator.compute_jacobian,
            generator_config=config,
        )


class CustomCudaRobotModel(CudaRobotModel):
    def _cuda_forward(self, q: torch.Tensor) -> Tuple[Tensor, Tensor, Tensor]:
        link_pos, link_quat, robot_spheres = custom_get_cuda_kinematics(
            self._link_pos_seq,
            self._link_quat_seq,
            self._batch_robot_spheres,
            self._global_cumul_mat,
            q,
            self.kinematics_config.fixed_transforms,
            self.kinematics_config.link_spheres,
            self.kinematics_config.link_map,  # tells which link is attached to which link i
            self.kinematics_config.joint_map,  # tells which joint is attached to a link i
            self.kinematics_config.joint_map_type,  # joint type
            self.kinematics_config.store_link_map,
            self.kinematics_config.link_sphere_idx_map,  # sphere idx map
            self.kinematics_config.link_chain_map,
            self.kinematics_config.joint_offset_map,
            self._grad_out_q,
            self.use_global_cumul,
        )
        return link_pos, link_quat, robot_spheres
