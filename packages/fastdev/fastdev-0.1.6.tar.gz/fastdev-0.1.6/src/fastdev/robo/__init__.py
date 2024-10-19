import warp as wp

from fastdev.robo.robot_model import RobotModel, RobotModelConfig

wp.config.quiet = True
wp.init()

__all__ = ["RobotModel", "RobotModelConfig"]
