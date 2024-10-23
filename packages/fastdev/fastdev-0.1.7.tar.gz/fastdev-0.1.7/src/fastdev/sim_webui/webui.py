# ruff: noqa: F821
import random
import string
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from itertools import chain
from pathlib import Path
from threading import Event
from typing import Dict, List, Literal, Optional, Tuple, Union, cast, overload

import numpy as np
import torch
import trimesh
import viser
from jaxtyping import Float, Integer, UInt

from fastdev.robo.robot_model import RobotModel
from fastdev.utils.tensor_utils import atleast_nd, to_number, to_numpy
from fastdev.xform.warp_rotation import matrix_to_quaternion_numpy

# fmt: off
_COMMON_COLORS: Dict[str, List[int]] = {
    "red": [255, 0, 0], "green": [0, 255, 0], "blue": [0, 0, 255],
    "yellow": [255, 255, 0], "cyan": [0, 255, 255], "magenta": [255, 0, 255],
    "white": [255, 255, 255], "black": [0, 0, 0], "gray": [128, 128, 128],
    "orange": [255, 128, 0], "purple": [128, 0, 128], "pink": [255, 0, 128],
    "brown": [128, 64, 0], "teal": [0, 128, 128], "navy": [0, 0, 128],
    "silver": [192, 192, 192], "gold": [255, 215, 0], "indigo": [74, 0, 130],
    "violet": [238, 130, 238], "skyblue": [135, 206, 250]
}
# fmt: on
_DEFAULT_ROBOT_COLOR = np.array([192, 192, 192], dtype=np.uint8)

AssetType = Literal["mesh", "robot", "point_cloud", "axes"]
JointValues = Float[np.ndarray, "num_frames num_dofs"]
JointValuesLike = Union[Float[np.ndarray, "*num_frames num_dofs"], Float[torch.Tensor, "*num_frames num_dofs"]]
Poses = Union[Float[np.ndarray, "*num_frames 4 4"], Float[np.ndarray, "*num_frames 7"]]
PosesLike = Union[
    Float[np.ndarray, "*num_frames 4 4"],
    Float[np.ndarray, "*num_frames 7"],
    Float[torch.Tensor, "*num_frames 4 4"],
    Float[torch.Tensor, "*num_frames 7"],
]
Vertices = Float[np.ndarray, "num_vertices 3"]
VerticesLike = Union[Float[np.ndarray, "*num_vertices 3"], Float[torch.Tensor, "*num_vertices 3"]]
FacesLike = Union[Integer[np.ndarray, "num_faces 3"], Integer[torch.Tensor, "num_faces 3"]]
Color = UInt[np.ndarray, "... 3"]
ColorLike = Union[
    str,
    List[int],
    List[float],
    Integer[np.ndarray, "... 3"],
    Float[np.ndarray, "... 3"],
    Integer[torch.Tensor, "... 3"],
    Float[torch.Tensor, "... 3"],
]
ScaleLike = Union[float, Float[np.ndarray, "..."], Float[torch.Tensor, "..."]]
AxesPositions = Float[np.ndarray, "num_axes 3"]
AxesPositionsLike = Union[Float[np.ndarray, "*num_axes 3"], Float[torch.Tensor, "*num_axes 3"]]
AxesWXYZs = Float[np.ndarray, "num_axes 4"]
AxesWXYZsLike = Union[
    Float[np.ndarray, "*num_axes 4"],
    Float[np.ndarray, "*num_axes 3 3"],
    Float[torch.Tensor, "*num_axes 4"],
    Float[torch.Tensor, "*num_axes 3 3"],
]


@dataclass
class ViserAsset:
    viser_asset_id: str
    viser_asset_type: Literal["trimesh", "point_cloud", "axes"]

    # for all assets
    color: Optional[Color] = None

    # for trimesh
    scale: float = 1.0
    trimesh_mesh: Optional[trimesh.Trimesh] = None

    # for point cloud
    points: Optional[Vertices] = None
    point_size: float = 0.02

    # for axes
    axes_positions: Optional[AxesPositions] = None
    axes_wxyzs: Optional[AxesWXYZs] = None
    axes_length: float = 0.1
    axes_radius: float = 0.005


@dataclass
class ViserAssetState:
    asset_id: str
    viser_asset_id: str
    position: Float[np.ndarray, "3"]
    wxyz: Float[np.ndarray, "4"]


@dataclass
class Asset(ABC):
    """Base asset class."""

    asset_id: str


@dataclass
class MeshAsset(Asset):
    trimesh_mesh: trimesh.Trimesh

    _viser_assets: Dict[str, ViserAsset] = field(default_factory=dict)
    _color_if_not_provided: Optional[Color] = None

    def get_viser_asset(self, viser_asset_id: str) -> ViserAsset:
        return self._viser_assets[viser_asset_id]

    def get_or_create_asset_id(self, color: Optional[Color], scale: float, postfix: int = 0) -> str:
        if color is None:
            if self._color_if_not_provided is None:
                self._color_if_not_provided = get_random_color()
            color = self._color_if_not_provided
        asset_id = f"mesh/{self.asset_id}/#{color[0]:02x}{color[1]:02x}{color[2]:02x}_{scale:.6f}_{postfix}"
        if asset_id not in self._viser_assets:
            mesh = self.trimesh_mesh.copy()
            mesh.visual.face_colors = color
            viser_asset = ViserAsset(
                viser_asset_id=asset_id,
                viser_asset_type="trimesh",
                trimesh_mesh=mesh,
                scale=scale,
            )
            self._viser_assets[asset_id] = viser_asset
        return asset_id


@dataclass
class PointCloudAsset(Asset):
    points: Vertices

    _viser_assets: Dict[str, ViserAsset] = field(default_factory=dict)
    _color_if_not_provided: Optional[Color] = None

    def get_viser_asset(self, viser_asset_id: str) -> ViserAsset:
        return self._viser_assets[viser_asset_id]

    def get_or_create_asset_id(self, color: Optional[Color], point_size: float) -> str:
        if color is None:
            if self._color_if_not_provided is None:
                self._color_if_not_provided = get_random_color()
            color = self._color_if_not_provided
        asset_id = f"pc/{self.asset_id}/#{color[0]:02x}{color[1]:02x}{color[2]:02x}_{point_size:.6f}"
        if asset_id not in self._viser_assets:
            viser_asset = ViserAsset(
                viser_asset_id=asset_id,
                viser_asset_type="point_cloud",
                points=self.points,
                point_size=point_size,
                color=color,
            )
            self._viser_assets[asset_id] = viser_asset
        return asset_id


@dataclass
class AxesAsset(Asset):
    positions: AxesPositions
    wxyzs: AxesWXYZs

    _viser_assets: Dict[str, ViserAsset] = field(default_factory=dict)

    def get_viser_asset(self, viser_asset_id: str) -> ViserAsset:
        return self._viser_assets[viser_asset_id]

    def get_or_create_asset_id(self, axes_length: float, axes_radius: float) -> str:
        asset_id = f"axes/{self.asset_id}/{axes_length:.6f}_{axes_radius:.6f}"
        if asset_id not in self._viser_assets:
            viser_asset = ViserAsset(
                viser_asset_id=asset_id,
                viser_asset_type="axes",
                axes_positions=self.positions,
                axes_wxyzs=self.wxyzs,
                axes_length=axes_length,
                axes_radius=axes_radius,
            )
            self._viser_assets[asset_id] = viser_asset
        return asset_id


@dataclass
class RobotAsset(Asset):
    robot_model: RobotModel

    _link_trimesh_meshes: Optional[Dict[str, trimesh.Trimesh]] = None
    _viser_assets: Dict[str, ViserAsset] = field(default_factory=dict)

    def get_viser_asset(self, viser_asset_id: str) -> ViserAsset:
        return self._viser_assets[viser_asset_id]

    def get_or_create_asset_id(self, link_name: str, color: Color) -> str:
        asset_id = f"robot/{self.asset_id}/{link_name}/#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
        if asset_id not in self._viser_assets:
            if self._link_trimesh_meshes is None:
                self._link_trimesh_meshes = self.robot_model.get_link_trimesh_meshes()
            mesh = self._link_trimesh_meshes[link_name].copy()
            mesh.visual.face_colors = color
            viser_asset = ViserAsset(
                viser_asset_id=asset_id,
                viser_asset_type="trimesh",
                trimesh_mesh=mesh,
            )
            self._viser_assets[asset_id] = viser_asset
        return asset_id


@dataclass
class AssetLibrary:
    """Asset library for multiple assets."""

    # assets
    _robot_assets: Dict[str, RobotAsset] = field(default_factory=dict)
    _mesh_assets: Dict[str, MeshAsset] = field(default_factory=dict)
    _pc_assets: Dict[str, PointCloudAsset] = field(default_factory=dict)
    _axes_assets: Dict[str, AxesAsset] = field(default_factory=dict)

    _asset_id_to_asset_type: Dict[str, AssetType] = field(default_factory=dict)
    _viser_assets: Dict[str, ViserAsset] = field(default_factory=dict)

    # cache for assets
    _urdf_or_mjcf_path_mesh_dir_to_robot_asset_id: Dict[Tuple[str, Optional[str]], str] = field(default_factory=dict)
    _trimesh_hash_to_mesh_asset_id: Dict[str, str] = field(default_factory=dict)
    _pc_array_hash_to_pc_asset_id: Dict[int, str] = field(default_factory=dict)
    _axes_hash_to_axes_asset_id: Dict[int, str] = field(default_factory=dict)

    def add_robot_asset(
        self,
        urdf_or_mjcf_path: str,
        mesh_dir: Optional[str] = None,
    ) -> str:
        if (urdf_or_mjcf_path, mesh_dir) not in self._urdf_or_mjcf_path_mesh_dir_to_robot_asset_id:
            robot_model = RobotModel.from_urdf_or_mjcf_path(urdf_or_mjcf_path, mesh_dir)
            robot_asset = RobotAsset(asset_id=self.get_random_asset_id(), robot_model=robot_model)
            self._robot_assets[robot_asset.asset_id] = robot_asset
            self._asset_id_to_asset_type[robot_asset.asset_id] = "robot"
            self._urdf_or_mjcf_path_mesh_dir_to_robot_asset_id[(urdf_or_mjcf_path, mesh_dir)] = robot_asset.asset_id
        return self._urdf_or_mjcf_path_mesh_dir_to_robot_asset_id[(urdf_or_mjcf_path, mesh_dir)]

    def add_mesh_asset(self, trimesh_mesh: trimesh.Trimesh, disable_cache: bool = False) -> str:
        if disable_cache:
            mesh_asset = MeshAsset(asset_id=self.get_random_asset_id(), trimesh_mesh=trimesh_mesh)
            self._mesh_assets[mesh_asset.asset_id] = mesh_asset
            self._asset_id_to_asset_type[mesh_asset.asset_id] = "mesh"
            return mesh_asset.asset_id
        else:
            trimesh_hash = trimesh_mesh.identifier_hash
            if trimesh_hash not in self._trimesh_hash_to_mesh_asset_id:
                mesh_asset = MeshAsset(asset_id=self.get_random_asset_id(), trimesh_mesh=trimesh_mesh)
                self._mesh_assets[mesh_asset.asset_id] = mesh_asset
                self._asset_id_to_asset_type[mesh_asset.asset_id] = "mesh"
                self._trimesh_hash_to_mesh_asset_id[trimesh_hash] = mesh_asset.asset_id
            return self._trimesh_hash_to_mesh_asset_id[trimesh_hash]

    def add_point_cloud_asset(self, points: Vertices) -> str:
        points_hash = hash(points.tobytes())
        if points_hash not in self._pc_array_hash_to_pc_asset_id:
            pc_asset = PointCloudAsset(asset_id=self.get_random_asset_id(), points=points)
            self._pc_assets[pc_asset.asset_id] = pc_asset
            self._asset_id_to_asset_type[pc_asset.asset_id] = "point_cloud"
            self._pc_array_hash_to_pc_asset_id[points_hash] = pc_asset.asset_id
        return self._pc_array_hash_to_pc_asset_id[points_hash]

    def add_axes_asset(
        self,
        positions: AxesPositions,
        wxyzs: AxesWXYZs,
    ) -> str:
        axes_hash = hash(positions.tobytes() + wxyzs.tobytes())
        if axes_hash not in self._axes_hash_to_axes_asset_id:
            axes_asset = AxesAsset(asset_id=self.get_random_asset_id(), positions=positions, wxyzs=wxyzs)
            self._axes_assets[axes_asset.asset_id] = axes_asset
            self._asset_id_to_asset_type[axes_asset.asset_id] = "axes"
            self._axes_hash_to_axes_asset_id[axes_hash] = axes_asset.asset_id
        return self._axes_hash_to_axes_asset_id[axes_hash]

    def asset_exists(self, asset_id: str) -> bool:
        asset_type = self._asset_id_to_asset_type.get(asset_id)
        if asset_type == "robot":
            return asset_id in self._robot_assets
        elif asset_type == "mesh":
            return asset_id in self._mesh_assets
        elif asset_type == "point_cloud":
            return asset_id in self._pc_assets
        elif asset_type == "axes":
            return asset_id in self._axes_assets
        return False

    def get_asset(self, asset_id: str) -> Asset:
        asset_type = self._asset_id_to_asset_type.get(asset_id)
        if asset_type == "robot":
            return self._robot_assets[asset_id]
        elif asset_type == "mesh":
            return self._mesh_assets[asset_id]
        elif asset_type == "point_cloud":
            return self._pc_assets[asset_id]
        elif asset_type == "axes":
            return self._axes_assets[asset_id]
        raise ValueError(f"Invalid asset type: {asset_type}")

    def get_viser_asset(self, asset_id: str, viser_asset_id: str) -> ViserAsset:
        if viser_asset_id not in self._viser_assets:
            asset_type = self._asset_id_to_asset_type.get(asset_id)
            if asset_type == "robot":
                self._viser_assets[viser_asset_id] = self._robot_assets[asset_id].get_viser_asset(viser_asset_id)
            elif asset_type == "mesh":
                self._viser_assets[viser_asset_id] = self._mesh_assets[asset_id].get_viser_asset(viser_asset_id)
            elif asset_type == "point_cloud":
                self._viser_assets[viser_asset_id] = self._pc_assets[asset_id].get_viser_asset(viser_asset_id)
            elif asset_type == "axes":
                self._viser_assets[viser_asset_id] = self._axes_assets[asset_id].get_viser_asset(viser_asset_id)
        return self._viser_assets[viser_asset_id]

    @staticmethod
    def get_random_asset_id() -> str:
        # ref: https://stackoverflow.com/a/56398787
        alphabet = string.ascii_lowercase + string.digits
        return "".join(random.choices(alphabet, k=8))


ASSET_LIBRARY = AssetLibrary()


def to_wxyz(rot: Optional[AxesWXYZsLike]) -> Float[np.ndarray, "... 4"]:
    rot = to_numpy(rot)
    if rot is None:
        return np.array([1.0, 0.0, 0.0, 0.0], dtype=np.float32)
    if rot.ndim >= 2 and rot.shape[-2:] == (3, 3):
        return matrix_to_quaternion_numpy(rot, scalar_first=True)
    elif rot.shape[-1] == 4:
        return rot
    else:
        raise ValueError(f"Invalid rotation shape: {rot.shape}")


def to_position_wxyz(pose: Optional[PosesLike]) -> Tuple[Float[np.ndarray, "... 3"], Float[np.ndarray, "... 4"]]:
    pose = to_numpy(pose)
    if pose is None:
        return np.zeros(3, dtype=np.float32), np.array([1.0, 0.0, 0.0, 0.0], dtype=np.float32)
    elif pose.shape[-2:] == (4, 4):
        position = pose[..., :3, 3]
        wxyz = matrix_to_quaternion_numpy(pose[..., :3, :3])
        return position, wxyz
    elif pose.shape[-1] == 7:
        return pose[..., :3], pose[..., 3:]
    else:
        raise ValueError(f"Invalid pose shape: {pose.shape}")


def get_random_color(
    r: Tuple[int, int] = (51, 180), g: Tuple[int, int] = (102, 204), b: Tuple[int, int] = (0, 102)
) -> Color:
    r_l = np.random.uniform(r[0], r[1], 1)
    g_l = np.random.uniform(g[0], g[1], 1)
    b_l = np.random.uniform(b[0], b[1], 1)
    return np.concatenate([r_l, g_l, b_l]).astype(np.uint8)


@overload
def to_color_array(color: None) -> None: ...
@overload
def to_color_array(color: ColorLike) -> Color: ...
def to_color_array(color: Optional[ColorLike]) -> Optional[Color]:
    if color is None:
        return None
    if isinstance(color, str):
        return np.array(_COMMON_COLORS[color]).astype(np.uint8)
    color = to_numpy(color, preserve_list=False)
    if color.dtype == np.float32 or color.dtype == np.float64:
        return (color * 255).astype(np.uint8)
    return color.astype(np.uint8)


@dataclass
class AssetState(ABC):
    """Asset state for multiple frames."""

    asset_id: str

    @property
    @abstractmethod
    def num_frames(self) -> int: ...

    @abstractmethod
    def get_frame_viser_asset_states(self, frame_index: int) -> List[ViserAssetState]: ...


@dataclass
class MeshState(AssetState):
    poses: Optional[Poses] = None
    color: Optional[Color] = None
    scale: float = 1.0

    @property
    def num_frames(self) -> int:
        return self.poses.shape[0] if self.poses is not None else 1

    def get_frame_viser_asset_states(self, frame_index: int) -> List[ViserAssetState]:
        mesh_asset: MeshAsset = cast(MeshAsset, ASSET_LIBRARY.get_asset(self.asset_id))
        pose = self.poses[frame_index] if self.poses is not None else None
        pos, wxyz = to_position_wxyz(pose)
        viser_asset_state = ViserAssetState(
            asset_id=self.asset_id,
            viser_asset_id=mesh_asset.get_or_create_asset_id(self.color, self.scale),
            position=pos,
            wxyz=wxyz,
        )
        return [viser_asset_state]


@dataclass
class PointCloudState(AssetState):
    poses: Optional[Poses] = None
    color: Optional[Color] = None
    point_size: float = 0.02

    @property
    def num_frames(self) -> int:
        return self.poses.shape[0] if self.poses is not None else 1

    def get_frame_viser_asset_states(self, frame_index: int) -> List[ViserAssetState]:
        pc_asset: PointCloudAsset = cast(PointCloudAsset, ASSET_LIBRARY.get_asset(self.asset_id))
        pose = self.poses[frame_index] if self.poses is not None else None
        pos, wxyz = to_position_wxyz(pose)
        viser_asset_state = ViserAssetState(
            asset_id=self.asset_id,
            viser_asset_id=pc_asset.get_or_create_asset_id(self.color, self.point_size),
            position=pos,
            wxyz=wxyz,
        )
        return [viser_asset_state]


@dataclass
class AxesState(AssetState):
    poses: Optional[Poses] = None
    axes_length: float = 0.1
    axes_radius: float = 0.005

    @property
    def num_frames(self) -> int:
        return self.poses.shape[0] if self.poses is not None else 1

    def get_frame_viser_asset_states(self, frame_index: int) -> List[ViserAssetState]:
        axes_asset: AxesAsset = cast(AxesAsset, ASSET_LIBRARY.get_asset(self.asset_id))
        pose = self.poses[frame_index] if self.poses is not None else None
        pos, wxyz = to_position_wxyz(pose)
        viser_asset_state = ViserAssetState(
            asset_id=self.asset_id,
            viser_asset_id=axes_asset.get_or_create_asset_id(
                axes_length=self.axes_length,
                axes_radius=self.axes_radius,
            ),
            position=pos,
            wxyz=wxyz,
        )
        return [viser_asset_state]


@dataclass
class RobotState(AssetState):
    joint_values: Optional[JointValues] = None
    root_poses: Optional[Poses] = None
    color: Color = field(default_factory=lambda: _DEFAULT_ROBOT_COLOR)

    @property
    def num_frames(self) -> int:
        return self.joint_values.shape[0] if self.joint_values is not None else 1

    def get_frame_viser_asset_states(self, frame_index: int) -> List[ViserAssetState]:
        robot_asset: RobotAsset = cast(RobotAsset, ASSET_LIBRARY.get_asset(self.asset_id))
        frame_joint_values = (
            self.joint_values[frame_index]
            if self.joint_values is not None
            else robot_asset.robot_model.get_zero_joint_values(return_tensors="np")
        )
        frame_root_poses = self.root_poses[frame_index] if self.root_poses is not None else None
        link_poses = robot_asset.robot_model.forward_kinematics_numpy(
            joint_values=frame_joint_values,  # type: ignore
            root_poses=frame_root_poses,  # type: ignore
        )
        viser_asset_states = []
        for link_name, link_pose in zip(robot_asset.robot_model.link_names, link_poses):
            link_pos, link_wxyz = to_position_wxyz(link_pose)
            viser_asset_states.append(
                ViserAssetState(
                    asset_id=self.asset_id,
                    viser_asset_id=robot_asset.get_or_create_asset_id(link_name, self.color),
                    position=link_pos,
                    wxyz=link_wxyz,
                )
            )
        return viser_asset_states


@dataclass
class SceneState:
    """Scene state for multiple assets and frames."""

    _num_frames: int = 0
    _last_updated: float = 0.0
    _robot_states: Dict[str, RobotState] = field(default_factory=dict)
    _mesh_states: Dict[str, MeshState] = field(default_factory=dict)
    _pc_states: Dict[str, PointCloudState] = field(default_factory=dict)
    _axes_states: Dict[str, AxesState] = field(default_factory=dict)

    def set_robot_state(
        self,
        asset_id: str,
        joint_values: Optional[JointValues] = None,
        root_poses: Optional[Poses] = None,
        color: Color = _DEFAULT_ROBOT_COLOR,
    ):
        robot_state = self._robot_states.get(asset_id, RobotState(asset_id=asset_id))
        robot_state.joint_values = joint_values
        robot_state.root_poses = root_poses
        robot_state.color = color
        if robot_state.num_frames > self._num_frames:
            self._num_frames = robot_state.num_frames
        self._robot_states[asset_id] = robot_state
        self._last_updated = time.time()

    def set_mesh_state(
        self,
        asset_id: str,
        poses: Optional[Poses] = None,
        scale: float = 1.0,
        color: Optional[Color] = None,
    ):
        mesh_state = self._mesh_states.get(asset_id, MeshState(asset_id=asset_id))
        mesh_state.poses = poses
        mesh_state.scale = scale
        mesh_state.color = color
        if mesh_state.num_frames > self._num_frames:
            self._num_frames = mesh_state.num_frames
        self._mesh_states[asset_id] = mesh_state
        self._last_updated = time.time()

    def set_point_cloud_state(
        self,
        asset_id: str,
        poses: Optional[Poses] = None,
        point_size: float = 0.02,
        color: Optional[Color] = None,
    ):
        pc_state = self._pc_states.get(asset_id, PointCloudState(asset_id=asset_id))
        pc_state.poses = poses
        pc_state.point_size = point_size
        pc_state.color = color
        if pc_state.num_frames > self._num_frames:
            self._num_frames = pc_state.num_frames
        self._pc_states[asset_id] = pc_state
        self._last_updated = time.time()

    def set_axes_state(
        self,
        asset_id: str,
        poses: Optional[Poses] = None,
        axes_length: float = 0.1,
        axes_radius: float = 0.005,
    ):
        axes_state = self._axes_states.get(asset_id, AxesState(asset_id=asset_id))
        axes_state.poses = poses
        axes_state.axes_length = axes_length
        axes_state.axes_radius = axes_radius
        if axes_state.num_frames > self._num_frames:
            self._num_frames = axes_state.num_frames
        self._axes_states[asset_id] = axes_state
        self._last_updated = time.time()

    @property
    def num_frames(self) -> int:
        return self._num_frames

    @property
    def last_updated(self) -> float:
        return self._last_updated

    def get_frame_viser_asset_states(self, frame_index: int) -> List[ViserAssetState]:
        viser_asset_states = []
        for asset_state in chain(
            self._robot_states.values(),
            self._mesh_states.values(),
            self._pc_states.values(),
            self._axes_states.values(),
        ):
            if asset_state.num_frames <= frame_index:
                continue
            viser_asset_states.extend(asset_state.get_frame_viser_asset_states(frame_index=frame_index))
        return viser_asset_states

    def __repr__(self) -> str:
        return (
            f"SceneState(num_frames={self.num_frames}, num_robot_states={len(self._robot_states)}, num_mesh_states={len(self._mesh_states)}, "
            f"num_pc_states={len(self._pc_states)}, num_axes_states={len(self._axes_states)})"
        )

    def __str__(self) -> str:
        return self.__repr__()


@dataclass
class StateManager:
    """State manager for multiple scenes."""

    _scene_states: List[SceneState] = field(default_factory=list)

    def set_robot_state(
        self,
        asset_id: str,
        scene_index: int,
        joint_values: Optional[JointValues] = None,
        root_poses: Optional[Poses] = None,
        color: Color = _DEFAULT_ROBOT_COLOR,
    ):
        self._get_scene_state(scene_index).set_robot_state(asset_id, joint_values, root_poses, color)

    def set_mesh_state(
        self,
        asset_id: str,
        scene_index: int,
        poses: Optional[Poses] = None,
        scale: float = 1.0,
        color: Optional[Color] = None,
    ):
        self._get_scene_state(scene_index).set_mesh_state(asset_id, poses, scale, color)

    def set_point_cloud_state(
        self,
        asset_id: str,
        scene_index: int,
        poses: Optional[Poses] = None,
        point_size: float = 1.0,
        color: Optional[Color] = None,
    ):
        self._get_scene_state(scene_index).set_point_cloud_state(asset_id, poses, point_size, color)

    def set_axes_state(
        self,
        asset_id: str,
        scene_index: int,
        poses: Optional[Poses] = None,
        axes_length: float = 0.1,
        axes_radius: float = 0.005,
    ):
        self._get_scene_state(scene_index).set_axes_state(asset_id, poses, axes_length, axes_radius)

    def _get_scene_state(self, scene_index: int) -> SceneState:
        if not self.validate_scene_index(scene_index):
            raise ValueError(f"Invalid scene index: {scene_index}")
        if scene_index == self.num_scenes:  # new scenes to be added
            self._scene_states.append(SceneState())
        return self._scene_states[scene_index]

    def get_scene_num_frames(self, scene_index: int) -> int:
        if len(self._scene_states) == 0:
            return 0
        return self._get_scene_state(scene_index).num_frames

    def get_scene_last_updated(self, scene_index: int) -> float:
        return self._get_scene_state(scene_index).last_updated

    def get_frame_viser_asset_states(self, scene_index: int, frame_index: int) -> List[ViserAssetState]:
        return self._get_scene_state(scene_index).get_frame_viser_asset_states(frame_index=frame_index)

    @property
    def num_scenes(self) -> int:
        return len(self._scene_states)

    def validate_scene_index(self, scene_index: int) -> bool:
        """Validate the scene index.

        Valid scene index should be in the range [0, num_scenes], including both ends.
        When the scene index equals to num_scenes, it means the scene is the new scene to be added.

        Args:
            scene_index (int): Scene index.
        """
        return 0 <= scene_index <= self.num_scenes

    def reset(self):
        self._scene_states = []

    def __getitem__(self, scene_index: int) -> SceneState:
        return self._get_scene_state(scene_index)

    def __repr__(self) -> str:
        return f"StateManager(num_scenes={self.num_scenes})"

    def __str__(self) -> str:
        return self.__repr__()


# thread-safe event for playing status
IS_PLAYING_EVENT = Event()


class ViserHelper:
    """Helper class for Viser server."""

    def __init__(
        self,
        state_manager: StateManager,
        host: str = "localhost",
        port: int = 8080,
        enable_geometry_option: bool = False,
    ):
        self._state_manager = state_manager

        self._viser_server = viser.ViserServer(host=host, port=port)
        self._viser_server.gui.configure_theme(control_width="large")

        self._gui_scene_folder = self._viser_server.gui.add_folder("Scene")
        with self._gui_scene_folder:
            self._gui_scene_index = self._viser_server.gui.add_slider("Index", min=0, max=0, step=1, initial_value=0)
            self._gui_scene_index.on_update(self.update_server)

        self._gui_frame_folder = self._viser_server.gui.add_folder("Frame")
        with self._gui_frame_folder:
            self._gui_is_playing = self._viser_server.gui.add_checkbox("Playing", False)
            self._gui_frame_index = self._viser_server.gui.add_slider("Index", min=0, max=0, step=1, initial_value=0)
            self._gui_is_playing.on_update(self.update_server)
            self._gui_frame_index.on_update(self.update_server)

        # TODO: support max_value property reading for sliders in viser
        self._scene_index = 0
        self._frame_index = 0
        self._max_scene_index_on_gui = 0
        self._max_frame_index_on_gui = 0
        self._is_playing = False
        self._scene_last_updated = 0.0
        IS_PLAYING_EVENT.clear()

        self._viser_asset_handles: Dict[str, viser.SceneNodeHandle] = {}
        self._visble_asset_handles: Dict[str, viser.SceneNodeHandle] = {}

    def update_server(self, *args, **kwargs):
        """Update the Viser server."""
        # TODO support max-value modification message on viser
        # TODO support client-side frame update for playing
        #    i.e., save frame history on the client side and update the frame index based on the playing status
        #    client only fetches the frame changes in the background and updates the changes to the history asynchronously

        # update max scene index on GUI if necessary
        max_scene_index_changed = self._max_scene_index_on_gui != self._state_manager.num_scenes - 1
        if max_scene_index_changed:
            with self._viser_server.atomic():
                with self._gui_scene_folder:
                    _cur_scene_index = self._gui_scene_index.value
                    self._gui_scene_index.remove()
                    self._gui_scene_index = self._viser_server.gui.add_slider(
                        "Index",
                        min=0,
                        max=max(self._state_manager.num_scenes - 1, 0),
                        step=1,
                        initial_value=max(0, min(_cur_scene_index, self._state_manager.num_scenes - 1)),
                    )
                    self._gui_scene_index.on_update(self.update_server)
                self._max_scene_index_on_gui = self._state_manager.num_scenes - 1

        # retrieve num_frames of the current scene
        scene_num_frames = self._state_manager.get_scene_num_frames(self._gui_scene_index.value)
        # remove & add `gui_frame_index` based on `is_playing`
        is_playing_changed = self._gui_is_playing.value != self._is_playing
        if is_playing_changed:
            with self._viser_server.atomic():
                if self._gui_is_playing.value:
                    # do not allow changing frame index when playing, remove the slider
                    self._gui_frame_index.remove()
                    IS_PLAYING_EVENT.set()
                else:
                    # add the slider back
                    with self._gui_frame_folder:
                        self._gui_frame_index = self._viser_server.gui.add_slider(
                            "Index",
                            min=0,
                            max=max(scene_num_frames - 1, 0),
                            step=1,
                            initial_value=max(0, min(self._frame_index, scene_num_frames - 1)),
                        )
                        self._gui_frame_index.on_update(self.update_server)
                        self._max_frame_index_on_gui = scene_num_frames - 1
                    IS_PLAYING_EVENT.clear()
                self._is_playing = self._gui_is_playing.value

        # update max frame index on GUI if necessary and not playing
        max_frame_index_changed = self._max_frame_index_on_gui != scene_num_frames - 1 and not self._is_playing
        if max_frame_index_changed:
            with self._viser_server.atomic():
                self._gui_frame_index.remove()
                with self._gui_frame_folder:
                    self._gui_frame_index = self._viser_server.gui.add_slider(
                        "Index",
                        min=0,
                        max=max(scene_num_frames - 1, 0),
                        step=1,
                        initial_value=max(0, min(self._frame_index, scene_num_frames - 1)),
                    )
                    self._gui_frame_index.on_update(self.update_server)
                    self._max_frame_index_on_gui = scene_num_frames - 1

        # -------------------- core logic --------------------
        # update asset states if necessary
        expected_num_frames = (
            self._gui_frame_index.value
            if not self._is_playing
            else max(0, min(self._frame_index + 1, scene_num_frames - 1))
        )
        scene_index_changed = self._scene_index != self._gui_scene_index.value
        frame_index_changed = self._frame_index != expected_num_frames
        scene_last_updated_changed = self._scene_last_updated != self._state_manager.get_scene_last_updated(
            self._gui_scene_index.value
        )
        if scene_index_changed or frame_index_changed or scene_last_updated_changed:
            new_visible_asset_handles: Dict[str, viser.SceneNodeHandle] = {}
            frame_asset_states = self._state_manager.get_frame_viser_asset_states(
                scene_index=self._gui_scene_index.value, frame_index=expected_num_frames
            )
            for asset_state in frame_asset_states:
                if asset_state.viser_asset_id not in self._viser_asset_handles:
                    self._add_viser_asset_from_state(asset_state)
                else:
                    self._update_viser_asset_from_state(asset_state)
                new_visible_asset_handles[asset_state.viser_asset_id] = self._viser_asset_handles[
                    asset_state.viser_asset_id
                ]
            # hide invisible assets
            for viser_asset_id, viser_asset_handle in self._visble_asset_handles.items():
                if viser_asset_id not in new_visible_asset_handles:
                    viser_asset_handle.visible = False
            self._visble_asset_handles = new_visible_asset_handles
            self._scene_index = self._gui_scene_index.value
            self._frame_index = expected_num_frames
            self._scene_last_updated = self._state_manager.get_scene_last_updated(self._gui_scene_index.value)

    def _add_viser_asset_from_state(self, asset_state: ViserAssetState):
        viser_asset = ASSET_LIBRARY.get_viser_asset(asset_state.asset_id, asset_state.viser_asset_id)
        if viser_asset.viser_asset_type == "trimesh":
            asset_handle = self._viser_server.scene.add_mesh_trimesh(
                name=viser_asset.viser_asset_id,
                mesh=viser_asset.trimesh_mesh,  # type: ignore
                position=asset_state.position,
                wxyz=asset_state.wxyz,
                scale=viser_asset.scale,
            )
        elif viser_asset.viser_asset_type == "point_cloud":
            asset_handle = self._viser_server.scene.add_point_cloud(
                name=viser_asset.viser_asset_id,
                points=viser_asset.points,  # type: ignore
                point_size=viser_asset.point_size,
                point_shape="circle",
                colors=viser_asset.color,  # type: ignore
            )
        elif viser_asset.viser_asset_type == "axes":
            asset_handle = self._viser_server.scene.add_batched_axes(
                name=viser_asset.viser_asset_id,
                batched_positions=viser_asset.axes_positions,  # type: ignore
                batched_wxyzs=viser_asset.axes_wxyzs,  # type: ignore
                axes_length=viser_asset.axes_length,
                axes_radius=viser_asset.axes_radius,
            )
        self._viser_asset_handles[viser_asset.viser_asset_id] = asset_handle

    def _update_viser_asset_from_state(self, asset_state: ViserAssetState):
        viser_asset_handle = self._viser_asset_handles[asset_state.viser_asset_id]
        with self._viser_server.atomic():
            # TODO support scale, color, etc in viser
            viser_asset_handle.position = asset_state.position
            viser_asset_handle.wxyz = asset_state.wxyz
            viser_asset_handle.visible = True

    def reset(self):
        self._scene_index = 0
        self._frame_index = 0
        self._scene_last_updated = 0.0

        # self._is_playing = False
        # IS_PLAYING_EVENT.clear()

        for viser_asset_handle in self._viser_asset_handles.values():
            viser_asset_handle.visible = False
        self._visble_asset_handles = {}


class SimWebUI:
    """WebUI for simulator and 3D scene visualization."""

    def __init__(self, host: str = "localhost", port: int = 8080, enable_geometry_option: bool = False):
        self._state_manager = StateManager()
        self._scene_index = 0
        self._viser_helper = ViserHelper(
            state_manager=self._state_manager,
            host=host,
            port=port,
            enable_geometry_option=enable_geometry_option,
        )

    def __repr__(self) -> str:
        return f"SimWebUI(scene_index={self._scene_index}, num_scenes={self._state_manager.num_scenes})"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def scene_index(self) -> int:
        return self._scene_index

    def set_scene_index(self, value: int):
        self._scene_index = value

    def add_robot_asset(
        self,
        urdf_or_mjcf_path: Union[str, Path],
        mesh_dir: Optional[Union[str, Path]] = None,
    ) -> str:
        """Add a robot asset to the asset library.

        Args:
            urdf_or_mjcf_path (Union[str, Path]): Path to the URDF or MJCF file of the robot.
            mesh_dir (Optional[Union[str, Path]], optional): Directory path of the robot meshes. Will use the directory of the URDF/MJCF file if not provided. Defaults to None.

        Returns:
            str: Asset ID of the robot asset.
        """
        if isinstance(urdf_or_mjcf_path, Path):
            urdf_or_mjcf_path = str(urdf_or_mjcf_path)
        if mesh_dir is not None and isinstance(mesh_dir, Path):
            mesh_dir = str(mesh_dir)
        return ASSET_LIBRARY.add_robot_asset(urdf_or_mjcf_path, mesh_dir)

    def add_mesh_asset(
        self,
        vertices: Optional[VerticesLike] = None,
        faces: Optional[FacesLike] = None,
        trimesh_mesh: Optional[trimesh.Trimesh] = None,
        mesh_path: Optional[Union[str, Path]] = None,
        disable_cache: bool = False,
    ) -> str:
        """Add a mesh asset to the asset library.

        Args:
            vertices (Optional[VerticesLike], optional): Vertices of the mesh. Defaults to None.
            faces (Optional[FacesLike], optional): Faces of the mesh. Defaults to None.
            trimesh_mesh (Optional[trimesh.Trimesh], optional): Trimesh mesh object. Defaults to None.
            mesh_path (Optional[Union[str, Path]], optional): Path to the mesh file. Defaults to None.

        Returns:
            str: Asset ID of the mesh asset.

        .. note::
            Either trimesh_mesh or vertices and faces or mesh_path must be provided, but not both.
        """
        trimesh_provided = trimesh_mesh is not None
        vertices_faces_provided = vertices is not None and faces is not None
        mesh_path_provided = mesh_path is not None
        if not (trimesh_provided ^ vertices_faces_provided ^ mesh_path_provided):
            raise ValueError("Either trimesh_mesh or vertices and faces or mesh_path must be provided.")
        if vertices_faces_provided:
            trimesh_mesh = trimesh.Trimesh(vertices=to_numpy(vertices), faces=to_numpy(faces))
        elif mesh_path_provided:
            trimesh_mesh = trimesh.load(mesh_path, process=False, force="mesh")  # type: ignore
        return ASSET_LIBRARY.add_mesh_asset(trimesh_mesh, disable_cache=disable_cache)  # type: ignore

    def add_sphere_asset(self, radius: ScaleLike, subdivisions: int = 3, disable_cache: bool = False) -> str:
        """Add a single sphere asset to the asset library.

        Args:
            radius (float): Radius of the sphere.
            subdivisions (int, optional): Number of subdivisions. Defaults to 3.

        Returns:
            str: Asset ID of the sphere asset.
        """
        radius = to_number(radius)
        sphere_mesh = trimesh.creation.icosphere(radius=radius, subdivisions=subdivisions)
        return ASSET_LIBRARY.add_mesh_asset(sphere_mesh, disable_cache=disable_cache)  # type: ignore

    def add_point_cloud_asset(self, points: VerticesLike) -> str:
        """Add a point cloud asset to the asset library.

        Args:
            points (VerticesLike): Points of the point cloud.

        Returns:
            str: Asset ID of the point cloud asset.
        """
        return ASSET_LIBRARY.add_point_cloud_asset(atleast_nd(to_numpy(points), expected_ndim=2))

    def add_axes_asset(self, positions: AxesPositionsLike, rotations: AxesWXYZsLike) -> str:
        """Add an axes asset to the asset library.

        Args:
            positions (AxesPositionLike): Positions of the axes.
            rotations (AxesWXYZsLike): Rotations of the axes, could be in rotation matrices or wxyz quaternions.

        Returns:
            str: Asset ID of the axes asset.
        """
        return ASSET_LIBRARY.add_axes_asset(
            positions=atleast_nd(to_numpy(positions), expected_ndim=2),
            wxyzs=atleast_nd(to_wxyz(rotations), expected_ndim=2),
        )

    def set_robot_state(
        self,
        asset_id: str,
        scene_index: Optional[int] = None,
        joint_values: Optional[JointValuesLike] = None,
        root_poses: Optional[PosesLike] = None,
        color: ColorLike = "silver",
    ):
        """Set the state of a robot asset.

        Args:
            asset_id (str): Asset ID of the robot asset.
            joint_values (Optional[JointValuesT], optional): Multi-frame (or single-frame) joint values. Defaults to None.
            root_poses (Optional[PosesT], optional): Multi-frame (or single-frame) root poses. Defaults to None.
            scene_index (Optional[int], optional): Scene index. Defaults to None.

        .. note::
            The number of frames of the asset state is determined by the number of joint values provided.
        """
        if not ASSET_LIBRARY.asset_exists(asset_id):
            raise ValueError(f"Asset with ID '{asset_id}' does not exist.")
        scene_index = scene_index if scene_index is not None else self.scene_index
        joint_values = atleast_nd(to_numpy(joint_values), expected_ndim=2)
        root_poses = atleast_nd(to_numpy(root_poses), expected_ndim=3)
        color = to_color_array(color)
        if joint_values is not None and root_poses is not None:
            if joint_values.shape[0] != root_poses.shape[0]:
                raise ValueError(
                    f"Number of frames mismatch, joint_values: {joint_values.shape[0]}, root_poses: {root_poses.shape[0]}"  # type: ignore
                )
        self._state_manager.set_robot_state(
            asset_id=asset_id,
            scene_index=scene_index,
            joint_values=joint_values,
            root_poses=root_poses,
            color=color,
        )
        self._viser_helper.update_server()

    def set_mesh_state(
        self,
        asset_id: str,
        scene_index: Optional[int] = None,
        poses: Optional[PosesLike] = None,
        scale: ScaleLike = 1.0,
        color: Optional[ColorLike] = None,
    ):
        """Set the state of a mesh asset.

        Args:
            asset_id (str): Asset ID of the mesh asset.
            scene_index (Optional[int], optional): Scene index. Defaults to None.
            poses (Optional[PosesLike], optional): Multi-frame (or single-frame) poses. Defaults to None.
            scale (ScaleLike, optional): Scale factor. Defaults to 1.0.
            color (ColorLike, optional): Color of the mesh, use random color if not provided. Defaults to None.

        .. note::
            The number of frames of the asset state is determined by the number of poses provided.
        """
        if not ASSET_LIBRARY.asset_exists(asset_id):
            raise ValueError(f"Asset with ID '{asset_id}' does not exist.")
        scene_index = scene_index if scene_index is not None else self.scene_index
        poses = atleast_nd(to_numpy(poses), expected_ndim=3)
        scale = to_number(scale)
        color = to_color_array(color)
        self._state_manager.set_mesh_state(
            asset_id=asset_id, scene_index=scene_index, poses=poses, scale=scale, color=color
        )
        self._viser_helper.update_server()

    def set_sphere_state(
        self,
        asset_id: str,
        scene_index: Optional[int] = None,
        poses: Optional[PosesLike] = None,
        scale: ScaleLike = 1.0,
        color: Optional[ColorLike] = None,
    ):
        """Set the state of a sphere asset.

        Args:
            asset_id (str): Asset ID of the sphere asset.
            scene_index (Optional[int], optional): Scene index. Defaults to None.
            poses (Optional[PosesLike], optional): Multi-frame (or single-frame) poses. Defaults to None.
            scale (ScaleLike, optional): Scale factor. Defaults to 1.0.
            color (Optional[ColorLike], optional): Color of the sphere. Defaults to None.

        .. note::
            The number of frames of the asset state is determined by the number of poses provided.
        """
        self.set_mesh_state(asset_id, scene_index, poses, scale, color)

    def set_point_cloud_state(
        self,
        asset_id: str,
        scene_index: Optional[int] = None,
        poses: Optional[PosesLike] = None,
        point_size: ScaleLike = 0.02,
        color: Optional[ColorLike] = None,
    ):
        """Set the state of a point cloud asset.

        Args:
            asset_id (str): Asset ID of the point cloud asset.
            scene_index (Optional[int], optional): Scene index. Defaults to None.
            poses (Optional[PosesLike], optional): Multi-frame (or single-frame) poses. Defaults to None.
            scale (ScaleLike, optional): Scale factor. Defaults to 1.0.
            color (Optional[ColorLike], optional): Color of the point cloud. Defaults to None.

        .. note::
            The number of frames of the asset state is determined by the number of poses provided.
        """
        if not ASSET_LIBRARY.asset_exists(asset_id):
            raise ValueError(f"Asset with ID '{asset_id}' does not exist.")
        scene_index = scene_index if scene_index is not None else self.scene_index
        poses = atleast_nd(to_numpy(poses), expected_ndim=3)
        point_size = to_number(point_size)
        color = to_color_array(color)
        if isinstance(color, np.ndarray) and color.ndim > 1:
            raise NotImplementedError("Batched colors for point clouds are not supported yet.")
        self._state_manager.set_point_cloud_state(
            asset_id=asset_id,
            scene_index=scene_index,
            poses=poses,
            point_size=point_size,
            color=color,
        )
        self._viser_helper.update_server()

    def set_axes_state(
        self,
        asset_id: str,
        scene_index: Optional[int] = None,
        axes_length: ScaleLike = 0.1,
        axes_radius: ScaleLike = 0.005,
        poses: Optional[PosesLike] = None,
    ):
        """Set the state of a point cloud asset.

        Args:
            asset_id (str): Asset ID of the point cloud asset.
            scene_index (Optional[int], optional): Scene index. Defaults to None.
            axes_length (ScaleLike, optional): Length of the axes. Defaults to 0.1.
            axes_radius (ScaleLike, optional): Radius of the axes. Defaults to 0.005.
            poses (Optional[PosesLike], optional): Multi-frame (or single-frame) poses. Defaults to None.

        .. note::
            The number of frames of the asset state is determined by the number of poses provided.
        """
        if not ASSET_LIBRARY.asset_exists(asset_id):
            raise ValueError(f"Asset with ID '{asset_id}' does not exist.")
        scene_index = scene_index if scene_index is not None else self.scene_index
        poses = atleast_nd(to_numpy(poses), expected_ndim=3)
        axes_length = to_number(axes_length)
        axes_radius = to_number(axes_radius)
        self._state_manager.set_axes_state(
            asset_id=asset_id,
            scene_index=scene_index,
            poses=poses,
            axes_length=axes_length,
            axes_radius=axes_radius,
        )
        self._viser_helper.update_server()

    def reset(self):
        """Reset the state manager and Viser server."""
        self._state_manager.reset()
        self._viser_helper.reset()
        self._scene_index = 0
        self._viser_helper.update_server()
