# mypy: disable-error-code="empty-body"
# ruff: noqa: F821
import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Tuple, Union, overload

import numpy as np
import torch
import transforms3d
import trimesh
import yourdfpy
from beartype import beartype
from jaxtyping import Float
from lxml import etree
from trimesh.util import concatenate

from fastdev.robo.kinematics import forward_kinematics as forward_kinematics_pt
from fastdev.robo.warp_kinematics import forward_kinematics as forward_kinematics_wp
from fastdev.robo.warp_kinematics import forward_kinematics_numpy as forward_kinematics_wp_np

logger = logging.getLogger("fastdev")


Device = Optional[Union[str, torch.device]]  # from torch.types import Device  # make mypy happy
ROOT_JOINT_NAME: str = "__root__"
LINK_SPEC_SIZE: int = 23


class Geometry(ABC):
    @abstractmethod
    def get_trimesh_mesh(self) -> trimesh.Trimesh: ...


@dataclass
class Box(Geometry):
    size: List[float]

    def get_trimesh_mesh(self) -> trimesh.Trimesh:
        return trimesh.creation.box(self.size)


@dataclass
class Cylinder(Geometry):
    radius: float
    length: float

    def get_trimesh_mesh(self) -> trimesh.Trimesh:
        return trimesh.creation.cylinder(radius=self.radius, height=self.length)


@dataclass
class Capsule(Geometry):
    radius: float
    length: float

    def get_trimesh_mesh(self) -> trimesh.Trimesh:
        return trimesh.creation.capsule(radius=self.radius, height=self.length)


@dataclass
class Sphere(Geometry):
    radius: float

    def get_trimesh_mesh(self) -> trimesh.Trimesh:
        return trimesh.creation.icosphere(subdivisions=3, radius=self.radius)


def _try_very_hard_to_find_mesh_path(mesh_filename: str, mesh_dir: Optional[str] = None) -> str:
    mesh_filename = mesh_filename.replace("package://", "")  # remove package://
    if mesh_dir is not None:
        for level in range(len(os.path.normpath(mesh_filename).split(os.path.sep))):
            mesh_filename = os.path.normpath(mesh_filename).split(os.path.sep, level)[-1]
            if os.path.exists(os.path.join(mesh_dir, mesh_filename)):
                return os.path.join(mesh_dir, mesh_filename)
    else:
        for level in range(len(os.path.normpath(mesh_filename).split(os.path.sep))):
            mesh_filename = os.path.normpath(mesh_filename).split(os.path.sep, level)[-1]
            if os.path.exists(mesh_filename):
                return mesh_filename
    raise FileNotFoundError(f"Mesh file not found: {mesh_filename=}, {mesh_dir=}")


@dataclass
class Mesh(Geometry):
    scale: List[float]

    filename: Optional[str] = None  # usually relative path
    mesh_dir: Optional[str] = None  # usually urdf/mjcf file directory
    is_collision_geometry: bool = False

    vertices: Optional[np.ndarray] = None  # unscaled vertices
    faces: Optional[np.ndarray] = None

    _scaled_trimesh_mesh: Optional[trimesh.Trimesh] = None

    def get_trimesh_mesh(self) -> trimesh.Trimesh:
        if self._scaled_trimesh_mesh is not None:
            return self._scaled_trimesh_mesh

        if self.vertices is not None and self.faces is not None:
            self._scaled_trimesh_mesh = trimesh.Trimesh(self.vertices * np.asarray(self.scale), self.faces)
        else:
            if self.filename is None:
                raise ValueError("Either filename or vertices and faces must be provided")
            mesh_path = _try_very_hard_to_find_mesh_path(self.filename, self.mesh_dir)
            mesh: trimesh.Trimesh = trimesh.load(mesh_path, force="mesh", skip_materials=self.is_collision_geometry)  # type: ignore
            mesh.apply_scale(self.scale)
            self._scaled_trimesh_mesh = mesh

        return self._scaled_trimesh_mesh


@dataclass
class Material:
    name: Optional[str] = None
    color: Optional[np.ndarray] = None
    texture: Optional[str] = None


@dataclass
class Visual:
    origin: np.ndarray
    geometry: Geometry
    name: Optional[str] = None
    material: Optional[Material] = None

    def get_trimesh_mesh(self) -> trimesh.Trimesh:
        mesh = self.geometry.get_trimesh_mesh()
        return mesh.apply_transform(self.origin)


@dataclass
class Collision:
    origin: np.ndarray
    geometry: Geometry
    name: Optional[str] = None

    def get_trimesh_mesh(self) -> trimesh.Trimesh:
        mesh = self.geometry.get_trimesh_mesh()
        return mesh.apply_transform(self.origin)


class JointType(Enum):
    ROOT = -1  # used for base link, which has no parent joint
    FIXED = 0
    PRISMATIC = 1
    REVOLUTE = 2  # aka. rotational


@dataclass(frozen=True)
@beartype
class Joint:
    name: str
    type: JointType
    origin: Float[np.ndarray, "4 4"]
    axis: Float[np.ndarray, "3"]
    limit: Optional[Float[np.ndarray, "2"]]

    parent_link_name: str
    child_link_name: str

    mimic_joint: Optional[str] = None
    mimic_multiplier: Optional[float] = None
    mimic_offset: Optional[float] = None

    def __post_init__(self):
        if self.origin.shape != (4, 4):
            raise ValueError(f"Invalid origin shape: {self.origin.shape}")
        if self.axis.shape != (3,):
            raise ValueError(f"Invalid axis shape: {self.axis.shape}")
        if self.limit is not None and self.limit.shape != (2,):
            raise ValueError(f"Invalid limit shape: {self.limit.shape}")


@dataclass(frozen=True)
@beartype
class Link:
    name: str
    visuals: List[Visual] = field(default_factory=list)
    collisions: List[Collision] = field(default_factory=list)

    joint_name: str = field(init=False)  # parent joint name in urdf

    def set_joint_name(self, joint_name: str):
        object.__setattr__(self, "joint_name", joint_name)

    def get_trimesh_mesh(self, mode: Literal["visual", "collision"] = "collision") -> trimesh.Trimesh:
        if mode == "visual":
            meshes = [visual.get_trimesh_mesh() for visual in self.visuals]
        elif mode == "collision":
            meshes = [collision.get_trimesh_mesh() for collision in self.collisions]
        else:
            raise ValueError(f"Unknown mode: {mode}")
        return concatenate(meshes)  # type: ignore


@dataclass
@beartype
class RobotModelConfig:
    """Robot model configuration."""

    urdf_or_mjcf_path: Union[str, Path]
    mesh_dir: Optional[str] = None
    format: Optional[Literal["urdf", "mjcf"]] = None  # will be inferred if not provided

    device: Device = "cpu"

    mjcf_assets: Optional[Dict[str, Any]] = None

    ee_link_names: Optional[List[str]] = None  # will be inferred if not provided
    enable_mimic_joints: bool = True  # if False, mimic joints will be considered as active joints, only for URDF
    enable_curobo: bool = False  # if True, will load curobo model, only for URDF & CUDA
    curobo_spheres: Dict[str, List[dict]] = field(default_factory=dict)  # only for curobo

    def __post_init__(self):
        if isinstance(self.urdf_or_mjcf_path, Path):
            self.urdf_or_mjcf_path = str(self.urdf_or_mjcf_path)
        if isinstance(self.mesh_dir, Path):
            self.mesh_dir = str(self.mesh_dir)
        if not os.path.exists(self.urdf_or_mjcf_path):
            raise FileNotFoundError(f"URDF/MJCF file not found: {self.urdf_or_mjcf_path}")
        if self.format is None:
            if self.urdf_or_mjcf_path.endswith(".urdf"):
                self.format = "urdf"
            elif self.urdf_or_mjcf_path.endswith(".xml"):
                self.format = "mjcf"
            else:
                raise ValueError(f"Unknown file format: {self.urdf_or_mjcf_path}")


@beartype
class RobotModel:
    """Robot model.

    Args:
        config (RobotModelConfig): Robot model configuration.

    Examples:
        >>> robot_model = RobotModel(RobotModelConfig(urdf_or_mjcf_path="assets/robot_description/panda.urdf", device="cpu"))
        >>> robot_model.num_dofs
        8
        >>> link_poses = robot_model.forward_kinematics(torch.zeros(1, robot_model.num_dofs))
        >>> torch.allclose(link_poses[0, -1, :3, 3], torch.tensor([0.0880, 0.0000, 0.8676]), atol=1e-3)
        True
    """

    base_link_name: str
    ee_link_names: List[str]
    link_names: List[str]
    num_links: int

    active_joint_names: List[str]
    num_dofs: int

    joint_map: Dict[str, Joint]
    link_map: Dict[str, Link]

    def __init__(self, config: RobotModelConfig):
        self.config = config
        self.device = config.device

        if config.format == "urdf":
            self.joint_map, self.link_map = self.parse_urdf()
        elif config.format == "mjcf":
            self.joint_map, self.link_map = self.parse_mjcf()
        else:
            raise ValueError(f"Unknown file format: {config.format}")

        # infer active joint names
        self.active_joint_names = [
            joint_name
            for joint_name, joint in self.joint_map.items()
            if joint.type not in [JointType.FIXED, JointType.ROOT]
        ]
        # filter out mimic joints
        if self.config.enable_mimic_joints:
            self.active_joint_names = [
                joint_name for joint_name in self.active_joint_names if self.joint_map[joint_name].mimic_joint is None
            ]
        # infer number of DOFs
        self.num_dofs = len(self.active_joint_names)
        # check if contains mimic joints
        self.has_mimic_joints: bool = any(
            self.joint_map[joint_name].mimic_joint is not None for joint_name in self.joint_map
        )
        # collect mimic joint
        if self.has_mimic_joints:
            self.mimic_joint_names: List[str] = []
            mimic_joint_indices, mimic_multipliers, mimic_offsets = [], [], []
            for joint_name in self.joint_map:
                if self.joint_map[joint_name].mimic_joint is not None:
                    self.mimic_joint_names.append(joint_name)

                    mimic_joint_indices.append(self.active_joint_names.index(self.joint_map[joint_name].mimic_joint))  # type: ignore
                    mimic_multipliers.append(self.joint_map[joint_name].mimic_multiplier)
                    mimic_offsets.append(self.joint_map[joint_name].mimic_offset)
            self._mimic_joint_indices_np: Optional[np.ndarray] = np.array(mimic_joint_indices, dtype=np.int64)
            self._mimic_multipliers_np: Optional[np.ndarray] = np.array(mimic_multipliers, dtype=np.float32)
            self._mimic_offsets_np: Optional[np.ndarray] = np.array(mimic_offsets, dtype=np.float32)
        else:
            self.mimic_joint_names = []
            self._mimic_joint_indices_np = None
            self._mimic_multipliers_np = None
            self._mimic_offsets_np = None

        # set base link name
        self.link_names = list(self.link_map.keys())
        self.num_links = len(self.link_names)
        self.base_link_name = self.joint_map[ROOT_JOINT_NAME].child_link_name
        # infer ee link names if not provided
        if isinstance(self.config.ee_link_names, list):
            pass
        if isinstance(self.config.ee_link_names, str):
            self.config.ee_link_names = [self.config.ee_link_names]
        elif self.config.ee_link_names is None:
            _link_names = list(self.link_map.keys())
            for joint in self.joint_map.values():
                if joint.parent_link_name in _link_names:
                    _link_names.remove(joint.parent_link_name)
            if len(_link_names) == 0:
                raise ValueError("Could not determine end effector link.")
            self.config.ee_link_names = _link_names
        self.ee_link_names = self.config.ee_link_names
        # sort all links in topological order
        cur_links = [self.base_link_name]
        topological_order = []
        while cur_links:
            next_links = []
            for link_name in cur_links:
                topological_order.append(link_name)
                for joint in self.joint_map.values():
                    if joint.parent_link_name == link_name:
                        next_links.append(joint.child_link_name)
            cur_links = next_links
        self._link_names_topological_order = topological_order

        # collect joint limits
        joint_limits = []
        if len(self.active_joint_names) == 0:
            self._joint_limits_np: Optional[np.ndarray] = None
        elif self.joint_map[self.active_joint_names[0]].limit is None:
            self._joint_limits_np = None
        else:
            for joint_name in self.active_joint_names:
                joint = self.joint_map[joint_name]
                if joint.limit is None:
                    raise ValueError(f"Joint {joint_name} has no limit")
                joint_limits.append(joint.limit)
            self._joint_limits_np = np.stack(joint_limits, axis=0)

        # lazy initialization
        self._mimic_joint_indices_pt: Optional[torch.Tensor] = None
        self._mimic_multipliers_pt: Optional[torch.Tensor] = None
        self._mimic_offsets_pt: Optional[torch.Tensor] = None
        self._joint_limits_pt: Optional[torch.Tensor] = None
        self._joint_origins_pt: Optional[torch.Tensor] = None
        self._joint_types_pt: Optional[torch.Tensor] = None
        self._joint_axes_np: Optional[np.ndarray] = None
        self._joint_axes_pt: Optional[torch.Tensor] = None
        self._link_indices_topological_order_np: Optional[np.ndarray] = None
        self._link_indices_topological_order_pt: Optional[torch.Tensor] = None
        self._link_joint_types_np: Optional[np.ndarray] = None
        self._link_joint_types_pt: Optional[torch.Tensor] = None
        self._link_joint_indices_np: Optional[np.ndarray] = None
        self._link_joint_indices_pt: Optional[torch.Tensor] = None
        self._link_joint_origins_np: Optional[np.ndarray] = None
        self._link_joint_origins_pt: Optional[torch.Tensor] = None
        self._parent_link_indices_np: Optional[np.ndarray] = None
        self._parent_link_indices_pt: Optional[torch.Tensor] = None

    def parse_urdf(self) -> Tuple[Dict[str, Joint], Dict[str, Link]]:
        def urdf_str_to_joint_type(joint_type_str: str) -> JointType:
            if joint_type_str == "fixed":
                return JointType.FIXED
            elif joint_type_str == "prismatic":
                return JointType.PRISMATIC
            elif joint_type_str == "revolute":
                return JointType.REVOLUTE
            else:
                raise ValueError(f"Unknown joint type: {joint_type_str}")

        def build_joint_from_urdf(joint_spec: yourdfpy.urdf.Joint) -> Joint:
            joint_type = urdf_str_to_joint_type(joint_spec.type)
            if (
                joint_spec.limit is not None
                and joint_spec.limit.lower is not None
                and joint_spec.limit.upper is not None
            ):
                limit = np.array([joint_spec.limit.lower, joint_spec.limit.upper], dtype=np.float32)
            else:
                limit = None
            origin = joint_spec.origin if joint_spec.origin is not None else np.eye(4, dtype=np.float32)
            return Joint(
                name=joint_spec.name,
                type=joint_type,
                origin=origin.astype(np.float32),
                axis=joint_spec.axis.astype(np.float32),
                limit=limit,
                parent_link_name=joint_spec.parent,
                child_link_name=joint_spec.child,
                mimic_joint=None if joint_spec.mimic is None else joint_spec.mimic.joint,
                mimic_multiplier=None if joint_spec.mimic is None else joint_spec.mimic.multiplier,
                mimic_offset=None if joint_spec.mimic is None else joint_spec.mimic.offset,
            )

        def build_geometry_from_urdf(
            urdf_geometry: yourdfpy.urdf.Geometry, mesh_dir: str, use_collision_geometry: bool = False
        ) -> Geometry:
            if urdf_geometry.box is not None:
                return Box(size=urdf_geometry.box.size.tolist())
            elif urdf_geometry.cylinder is not None:
                return Cylinder(radius=urdf_geometry.cylinder.radius, length=urdf_geometry.cylinder.length)
            elif urdf_geometry.sphere is not None:
                return Sphere(radius=urdf_geometry.sphere.radius)
            elif urdf_geometry.mesh is not None:
                scale_spec = urdf_geometry.mesh.scale
                if isinstance(scale_spec, float):
                    scale: List[float] = [scale_spec, scale_spec, scale_spec]
                elif isinstance(scale_spec, np.ndarray):
                    scale = scale_spec.tolist()
                elif scale_spec is None:
                    scale = [1.0, 1.0, 1.0]
                else:
                    raise ValueError(f"Unknown scale type: {scale_spec}")
                return Mesh(
                    filename=urdf_geometry.mesh.filename,
                    mesh_dir=mesh_dir,
                    scale=scale,
                    is_collision_geometry=use_collision_geometry,
                )
            else:
                raise ValueError(f"Unknown geometry type: {urdf_geometry}")

        def build_material_from_urdf(urdf_material: yourdfpy.urdf.Material) -> Material:
            return Material(
                name=urdf_material.name,
                color=urdf_material.color.rgba if urdf_material.color is not None else None,
                texture=urdf_material.texture.filename if urdf_material.texture is not None else None,
            )

        def build_link_from_urdf(link_spec: yourdfpy.urdf.Link, mesh_dir: str) -> Link:
            link = Link(name=link_spec.name)
            for visual_spec in link_spec.visuals:
                assert visual_spec.geometry is not None, f"Visual {visual_spec.name} has no geometry"
                if visual_spec.origin is None:
                    origin = np.eye(4, dtype=np.float32)
                else:
                    origin = visual_spec.origin
                visual = Visual(
                    origin=origin,
                    geometry=build_geometry_from_urdf(
                        visual_spec.geometry, mesh_dir=mesh_dir, use_collision_geometry=False
                    ),
                    name=visual_spec.name,
                    material=build_material_from_urdf(visual_spec.material)
                    if visual_spec.material is not None
                    else None,
                )
                link.visuals.append(visual)
            for collision_spec in link_spec.collisions:
                if collision_spec.origin is None:
                    origin = np.eye(4, dtype=np.float32)
                else:
                    origin = collision_spec.origin
                collision = Collision(
                    origin=origin,
                    geometry=build_geometry_from_urdf(
                        collision_spec.geometry, mesh_dir=mesh_dir, use_collision_geometry=True
                    ),
                    name=collision_spec.name,
                )
                link.collisions.append(collision)
            return link

        if self.config.mesh_dir is None:
            self.config.mesh_dir = os.path.abspath(os.path.dirname(self.config.urdf_or_mjcf_path))

        # parse URDF
        urdf = yourdfpy.URDF.load(
            self.config.urdf_or_mjcf_path,
            load_meshes=False,
            build_scene_graph=False,
            mesh_dir=self.config.mesh_dir,
            filename_handler=yourdfpy.filename_handler_null,
        )

        # build joint maps
        joint_map: Dict[str, Joint] = {
            joint_name: build_joint_from_urdf(joint_spec) for joint_name, joint_spec in urdf.joint_map.items()
        }
        # infer base link name
        link_names: List[str] = list(urdf.link_map.keys())
        for joint in joint_map.values():
            if joint.child_link_name in link_names:
                link_names.remove(joint.child_link_name)
        if len(link_names) != 1:
            raise ValueError(f"Expected exactly one base link, got {len(link_names)}")
        base_link_name = link_names[0]
        # add a root joint for base link
        joint_map[ROOT_JOINT_NAME] = Joint(
            name=ROOT_JOINT_NAME,
            type=JointType.ROOT,
            origin=np.eye(4, dtype=np.float32),
            axis=np.zeros(3, dtype=np.float32),
            limit=np.array([0.0, 0.0], dtype=np.float32),
            parent_link_name="",
            child_link_name=base_link_name,
        )

        # build link maps
        link_map = {
            link_name: build_link_from_urdf(link_spec, mesh_dir=self.config.mesh_dir)
            for link_name, link_spec in urdf.link_map.items()
        }
        # set parent joint names for links
        for joint_name, joint in joint_map.items():
            link_map[joint.child_link_name].set_joint_name(joint_name)

        return joint_map, link_map

    def parse_mjcf(self) -> Tuple[Dict[str, Joint], Dict[str, Link]]:
        def is_collision_geometry(geom_spec) -> Optional[bool]:
            if geom_spec.contype is None or geom_spec.conaffinity is None:
                return None
            return geom_spec.contype ^ geom_spec.conaffinity

        def build_geometry_from_mjcf(geom_spec, use_collision_geometry: bool = True) -> Geometry:
            if geom_spec.type == "box":
                return Box(size=geom_spec.size * 2)
            elif geom_spec.type == "cylinder":
                raise NotImplementedError("Cylinder geometry is not supported in MJCF")
            elif geom_spec.type == "mesh" or geom_spec.mesh is not None:
                scale_spec = geom_spec.mesh.scale
                if isinstance(scale_spec, float):
                    scale: List[float] = [scale_spec, scale_spec, scale_spec]
                elif isinstance(scale_spec, np.ndarray):
                    scale = scale_spec.tolist()
                elif scale_spec is None:
                    scale = [1.0, 1.0, 1.0]
                else:
                    raise ValueError(f"Unknown scale type: {scale_spec}")
                mesh: trimesh.Trimesh = trimesh.load(  # type: ignore
                    trimesh.util.wrap_as_stream(geom_spec.mesh.file.contents),
                    file_type=geom_spec.mesh.file.extension.replace(".", ""),
                    force="mesh",
                    skip_materials=use_collision_geometry,
                )
                mesh.apply_scale(scale)
                return Mesh(scale=scale, _scaled_trimesh_mesh=mesh, is_collision_geometry=use_collision_geometry)
            elif geom_spec.type == "capsule":
                return Capsule(radius=geom_spec.size[0], length=geom_spec.size[1] * 2)
            elif geom_spec.type == "sphere" or geom_spec.type is None:
                return Sphere(radius=geom_spec.size)
            else:
                raise ValueError(f"Unknown geometry type: {geom_spec.type}")

        def build_pose_from_mjcf(quat: Optional[np.ndarray], pos: Optional[np.ndarray]) -> np.ndarray:
            # rot_mat = quaternion_to_matrix(to_torch(quat)) if quat is not None else torch.eye(3)
            # return to_numpy(rot_tl_to_tf_mat(rot_mat=rot_mat, tl=to_torch(pos)))
            rot_mat = transforms3d.quaternions.quat2mat(quat) if quat is not None else np.eye(3)
            tf_mat = np.eye(4)
            tf_mat[:3, :3] = rot_mat
            tf_mat[:3, 3] = pos if pos is not None else 0.0
            return tf_mat

        def build_link_from_mjcf(link_spec) -> Link:
            link = Link(name=link_spec.name)
            for geom in link_spec.geom:
                origin = build_pose_from_mjcf(geom.quat, geom.pos)
                is_collision = is_collision_geometry(geom)
                if is_collision is None or is_collision:
                    collision = Collision(
                        origin=origin,
                        geometry=build_geometry_from_mjcf(geom, use_collision_geometry=True),
                        name=geom.name,
                    )
                    link.collisions.append(collision)
                elif is_collision is None or not is_collision:
                    visual = Visual(origin=origin, geometry=build_geometry_from_mjcf(geom), name=geom.name)
                    link.visuals.append(visual)
            return link

        def mjcf_str_to_joint_type(joint_type_str: Optional[str] = "hinge") -> JointType:
            # https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint
            if joint_type_str == "fixed":
                return JointType.FIXED
            elif joint_type_str == "slide":
                return JointType.PRISMATIC
            elif joint_type_str == "hinge" or joint_type_str is None:
                return JointType.REVOLUTE
            else:
                raise ValueError(f"Unknown joint type: {joint_type_str}")

        def build_joint_from_mjcf(joint_spec, origin: np.ndarray, parent_link_name: str, child_link_name: str) -> Joint:
            joint_type = mjcf_str_to_joint_type(joint_spec.type)
            if joint_spec.range is not None:
                limit = np.asarray(joint_spec.range, dtype=np.float32)
            else:
                limit = None
            if joint_spec.axis is None:
                axis = np.asarray([0.0, 0.0, 1.0], dtype=np.float32)
            else:
                axis = np.asarray(joint_spec.axis, dtype=np.float32)
            return Joint(
                name=joint_spec.name,
                type=joint_type,
                origin=np.asarray(origin, dtype=np.float32),
                axis=axis,
                limit=limit,
                parent_link_name=parent_link_name,
                child_link_name=child_link_name,
            )

        try:
            import warnings

            from absl import flags

            # ignore annoying warning from dm_control
            warnings.filterwarnings("ignore", message=".*X11: The DISPLAY environment variable is missing.*")

            for name in list(flags.FLAGS):
                if "pymjcf" in name:
                    delattr(flags.FLAGS, name)

            import dm_control.mjcf
        except ImportError:
            raise ImportError("dm_control is required to parse MJCF files, please install by `pip install dm_control`")

        if self.config.mesh_dir is None:
            self.config.mesh_dir = os.path.dirname(self.config.urdf_or_mjcf_path)

        # The mjcf file by IsaacGym does not follow the convention of mujoco mjcf precisely
        # We need to handle it separately when the mjcf file is not valid by normal mjcf parser
        try:
            with open(self.config.urdf_or_mjcf_path, "r") as f:
                mjcf = dm_control.mjcf.from_file(f, assets=self.config.mjcf_assets, model_dir=self.config.mesh_dir)
        except KeyError:
            file_root = os.path.dirname(self.config.urdf_or_mjcf_path)
            tree = etree.parse(self.config.urdf_or_mjcf_path)  # type: ignore
            root = tree.getroot()
            invalid_includes = root.findall("*/include")
            for include in invalid_includes:
                parent = include.getparent()
                file: str = include.get("file")
                child_xml = etree.parse(os.path.join(file_root, file)).getroot().getchildren()  # type: ignore
                parent.remove(include)
                parent.extend(child_xml)

            xml_string = etree.tostring(tree)
            mjcf = dm_control.mjcf.from_xml_string(xml_string, model_dir=self.config.mesh_dir)

        # Substitute geom with default values
        for geom in mjcf.find_all("geom"):
            dm_control.mjcf.commit_defaults(geom)

        base_link_spec = mjcf.worldbody.body[0]  # type: ignore
        base_link_name = str(base_link_spec.name)

        link_map: Dict[str, Link] = {}
        joint_map: Dict[str, Joint] = {}
        link_specs = [(base_link_spec, "")]
        while link_specs:
            link_spec, parent_link_name = link_specs.pop()
            link_map[link_spec.name] = build_link_from_mjcf(link_spec)
            if len(link_spec.joint) > 0:
                if len(link_spec.joint) > 1:
                    raise ValueError(f"Link {link_spec.name} has multiple joints")
                joint_map[link_spec.joint[0].name] = build_joint_from_mjcf(
                    link_spec.joint[0],
                    origin=build_pose_from_mjcf(link_spec.quat, link_spec.pos),
                    parent_link_name=parent_link_name,
                    child_link_name=link_spec.name,
                )
                link_map[link_spec.name].set_joint_name(link_spec.joint[0].name)
            else:
                fixed_joint = Joint(
                    name=f"{link_spec.name}_fixed",
                    type=JointType.FIXED,
                    origin=np.eye(4, dtype=np.float32),
                    axis=np.zeros(3, dtype=np.float32),
                    limit=np.array([0.0, 0.0], dtype=np.float32),
                    parent_link_name=parent_link_name,
                    child_link_name=link_spec.name,
                )
                joint_map[fixed_joint.name] = fixed_joint
                link_map[link_spec.name].set_joint_name(fixed_joint.name)
            link_specs.extend([(child_link, link_spec.name) for child_link in link_spec.body])
        # add a root joint for base link
        joint_map[ROOT_JOINT_NAME] = Joint(
            name=ROOT_JOINT_NAME,
            type=JointType.ROOT,
            origin=np.eye(4, dtype=np.float32),
            axis=np.zeros(3, dtype=np.float32),
            limit=np.array([0.0, 0.0], dtype=np.float32),
            parent_link_name="",
            child_link_name=base_link_name,
        )
        link_map[base_link_name].set_joint_name(ROOT_JOINT_NAME)
        return joint_map, link_map

    @staticmethod
    def from_urdf_or_mjcf_path(
        urdf_or_mjcf_path: Union[str, Path], mesh_dir: Optional[str] = None, device: Device = "cpu"
    ) -> "RobotModel":
        return RobotModel(RobotModelConfig(urdf_or_mjcf_path=urdf_or_mjcf_path, mesh_dir=mesh_dir, device=device))

    def get_link_trimesh_meshes(
        self, mode: Literal["visual", "collision"] = "collision", return_empty_meshes: bool = True
    ) -> Dict[str, trimesh.Trimesh]:
        meshes = {link_name: self.link_map[link_name].get_trimesh_mesh(mode=mode) for link_name in self.link_names}
        if not return_empty_meshes:
            meshes = {n: m for n, m in meshes.items() if len(m.vertices) > 0 and len(m.faces) > 0}
        return meshes

    @overload
    def get_joint_limits(self, return_tensors: Literal["np"]) -> Optional[np.ndarray]: ...
    @overload
    def get_joint_limits(self, return_tensors: Literal["pt"] = "pt") -> Optional[torch.Tensor]: ...
    def get_joint_limits(self, return_tensors: Literal["np", "pt"] = "np") -> Optional[Union[np.ndarray, torch.Tensor]]:
        if return_tensors == "np":
            return self._joint_limits_np
        elif return_tensors == "pt":
            if self._joint_limits_pt is None and self._joint_limits_np is not None:
                self._joint_limits_pt = torch.from_numpy(self._joint_limits_np).to(self.device)
            return self._joint_limits_pt
        else:
            raise ValueError(f"Unknown return_tensors: {return_tensors}")

    @property
    def joint_limits(self) -> Optional[torch.Tensor]:
        return self.get_joint_limits(return_tensors="pt")

    @property
    def joint_axes(self) -> torch.Tensor:
        return self.get_joint_axes(return_tensors="pt")

    @overload
    def get_joint_axes(self, return_tensors: Literal["np"]) -> np.ndarray: ...
    @overload
    def get_joint_axes(self, return_tensors: Literal["pt"]) -> torch.Tensor: ...
    def get_joint_axes(self, return_tensors: Literal["np", "pt"] = "np") -> Union[np.ndarray, torch.Tensor]:
        if self._joint_axes_np is None:
            self._joint_axes_np = np.stack(
                [self.joint_map[joint_name].axis for joint_name in self.active_joint_names + self.mimic_joint_names],
                axis=0,
            )
        if return_tensors == "np":
            return self._joint_axes_np
        elif return_tensors == "pt":
            if self._joint_axes_pt is None:
                self._joint_axes_pt = torch.from_numpy(self._joint_axes_np).to(device=self.device, dtype=torch.float32)
            return self._joint_axes_pt

    @property
    def joint_origins(self) -> torch.Tensor:
        if self._joint_origins_pt is None:
            joint_origins = np.stack(
                [self.joint_map[joint_name].origin for joint_name in self.active_joint_names + self.mimic_joint_names],
                axis=0,
            )
            self._joint_origins_pt = torch.from_numpy(joint_origins).to(device=self.device, dtype=torch.float32)
        return self._joint_origins_pt

    @property
    def joint_types(self) -> torch.Tensor:
        if self._joint_types_pt is None:
            joint_types = [
                self.joint_map[joint_name].type.value for joint_name in self.active_joint_names + self.mimic_joint_names
            ]
            self._joint_types_pt = torch.tensor(joint_types, device=self.device, dtype=torch.int32)
        return self._joint_types_pt

    @property
    def link_joint_indices(self) -> torch.Tensor:
        return self.get_link_joint_indices(return_tensors="pt")

    @overload
    def get_link_joint_indices(self, return_tensors: Literal["np"]) -> np.ndarray: ...
    @overload
    def get_link_joint_indices(self, return_tensors: Literal["pt"]) -> torch.Tensor: ...
    def get_link_joint_indices(self, return_tensors: Literal["np", "pt"] = "np") -> Union[np.ndarray, torch.Tensor]:
        if self._link_joint_indices_np is None:
            full_joint_names = self.active_joint_names + self.mimic_joint_names
            link_joint_indices = []
            for link_name in self.link_names:
                joint_name = self.link_map[link_name].joint_name
                if joint_name not in full_joint_names:
                    link_joint_indices.append(-1)
                else:
                    link_joint_indices.append(full_joint_names.index(joint_name))
            self._link_joint_indices_np = np.array(link_joint_indices, dtype=np.int32)
        if return_tensors == "np":
            return self._link_joint_indices_np
        elif return_tensors == "pt":
            if self._link_joint_indices_pt is None:
                self._link_joint_indices_pt = torch.from_numpy(self._link_joint_indices_np).to(device=self.device)
            return self._link_joint_indices_pt

    @property
    def link_joint_types(self) -> torch.Tensor:
        return self.get_link_joint_types(return_tensors="pt")

    @overload
    def get_link_joint_types(self, return_tensors: Literal["np"]) -> np.ndarray: ...
    @overload
    def get_link_joint_types(self, return_tensors: Literal["pt"]) -> torch.Tensor: ...
    def get_link_joint_types(self, return_tensors: Literal["np", "pt"] = "np") -> Union[np.ndarray, torch.Tensor]:
        if self._link_joint_types_np is None:
            link_joint_types = [
                self.joint_map[self.link_map[link_name].joint_name].type.value for link_name in self.link_names
            ]
            self._link_joint_types_np = np.array(link_joint_types, dtype=np.int32)
        if return_tensors == "np":
            return self._link_joint_types_np
        elif return_tensors == "pt":
            if self._link_joint_types_pt is None:
                self._link_joint_types_pt = torch.from_numpy(self._link_joint_types_np).to(device=self.device)
            return self._link_joint_types_pt

    @property
    def link_joint_origins(self) -> torch.Tensor:
        return self.get_link_joint_origins(return_tensors="pt")

    @overload
    def get_link_joint_origins(self, return_tensors: Literal["np"]) -> np.ndarray: ...
    @overload
    def get_link_joint_origins(self, return_tensors: Literal["pt"]) -> torch.Tensor: ...
    def get_link_joint_origins(self, return_tensors: Literal["np", "pt"] = "np") -> Union[np.ndarray, torch.Tensor]:
        if self._link_joint_origins_np is None:
            link_joint_origins = [
                self.joint_map[self.link_map[link_name].joint_name].origin for link_name in self.link_names
            ]
            self._link_joint_origins_np = np.stack(link_joint_origins, axis=0)
        if return_tensors == "np":
            return self._link_joint_origins_np
        elif return_tensors == "pt":
            if self._link_joint_origins_pt is None:
                self._link_joint_origins_pt = torch.from_numpy(self._link_joint_origins_np).to(
                    device=self.device, dtype=torch.float32
                )
            return self._link_joint_origins_pt

    @property
    def link_indices_topological_order(self) -> torch.Tensor:
        return self.get_link_indices_topological_order(return_tensors="pt")

    @overload
    def get_link_indices_topological_order(self, return_tensors: Literal["np"]) -> np.ndarray: ...
    @overload
    def get_link_indices_topological_order(self, return_tensors: Literal["pt"]) -> torch.Tensor: ...
    def get_link_indices_topological_order(
        self, return_tensors: Literal["np", "pt"] = "np"
    ) -> Union[np.ndarray, torch.Tensor]:
        if self._link_indices_topological_order_np is None:
            link_indices = [self.link_names.index(link_name) for link_name in self._link_names_topological_order]
            self._link_indices_topological_order_np = np.array(link_indices, dtype=np.int32)
        if return_tensors == "np":
            return self._link_indices_topological_order_np
        elif return_tensors == "pt":
            if self._link_indices_topological_order_pt is None:
                self._link_indices_topological_order_pt = torch.from_numpy(self._link_indices_topological_order_np).to(
                    device=self.device
                )
            return self._link_indices_topological_order_pt

    @property
    def parent_link_indices(self) -> torch.Tensor:
        return self.get_parent_link_indices(return_tensors="pt")

    @overload
    def get_parent_link_indices(self, return_tensors: Literal["np"]) -> np.ndarray: ...
    @overload
    def get_parent_link_indices(self, return_tensors: Literal["pt"]) -> torch.Tensor: ...
    def get_parent_link_indices(self, return_tensors: Literal["np", "pt"] = "np") -> Union[np.ndarray, torch.Tensor]:
        if self._parent_link_indices_np is None:
            parent_link_indices = []
            for link_name in self.link_names:
                joint = self.joint_map[self.link_map[link_name].joint_name]
                if joint.type == JointType.ROOT:
                    parent_link_indices.append(-1)
                else:
                    parent_link_indices.append(self.link_names.index(joint.parent_link_name))
            self._parent_link_indices_np = np.array(parent_link_indices, dtype=np.int32)
        if return_tensors == "np":
            return self._parent_link_indices_np
        elif return_tensors == "pt":
            self._parent_link_indices_pt = torch.from_numpy(self._parent_link_indices_np).to(device=self.device)
            return self._parent_link_indices_pt

    def apply_mimic_joints(
        self, joint_values: Float[torch.Tensor, "*b num_dofs"]
    ) -> Float[torch.Tensor, "*b num_joints"]:
        if not self.has_mimic_joints:
            return joint_values
        else:
            if self._mimic_joint_indices_pt is None:
                self._mimic_joint_indices_pt = torch.from_numpy(self._mimic_joint_indices_np).to(device=self.device)
            if self._mimic_multipliers_pt is None:
                self._mimic_multipliers_pt = torch.from_numpy(self._mimic_multipliers_np).to(device=self.device)
            if self._mimic_offsets_pt is None:
                self._mimic_offsets_pt = torch.from_numpy(self._mimic_offsets_np).to(device=self.device)

            mimic_joint_values = torch.index_select(
                joint_values,
                index=self._mimic_joint_indices_pt.to(joint_values.device),  # type: ignore
                dim=-1,
            )
            mimic_joint_values = mimic_joint_values * self._mimic_multipliers_pt.to(  # type: ignore
                joint_values.device
            ) + self._mimic_offsets_pt.to(joint_values.device)  # type: ignore
            joint_values = torch.cat([joint_values, mimic_joint_values], dim=-1)
            return joint_values

    def forward_kinematics(
        self,
        joint_values: Float[torch.Tensor, "*b num_dofs"],
        joint_names: Optional[List[str]] = None,
        root_poses: Optional[Float[torch.Tensor, "*b 4 4"]] = None,
        clamp_joint_values: bool = True,
        use_warp: bool = True,
    ) -> Float[torch.Tensor, "*b num_links 4 4"]:
        """Forward kinematics.

        Args:
            joint_values (torch.Tensor): Joint values of shape (batch_size, num_dofs).
            joint_names (list of str, optional): Joint names. Defaults to None.
            root_poses (torch.Tensor, optional): Root poses of shape (batch_size, 4, 4). Defaults to None.
            clamp_joint_values (bool, optional): Whether to clamp joint values to joint limits. Defaults to True.

        """
        if joint_names is not None:
            joint_reindex = torch.tensor(
                [joint_names.index(joint_name) for joint_name in self.active_joint_names],
                device=joint_values.device,
                dtype=torch.long,
            )
            joint_values = torch.index_select(joint_values, dim=-1, index=joint_reindex)
        if clamp_joint_values and self._joint_limits_pt is not None:
            joint_values = torch.clamp(
                joint_values,
                self._joint_limits_pt[:, 0].to(device=joint_values.device),
                self._joint_limits_pt[:, 1].to(device=joint_values.device),
            )
        if self.has_mimic_joints:
            joint_values = self.apply_mimic_joints(joint_values)
        if use_warp:
            link_poses = forward_kinematics_wp(joint_values, robot_model=self)
        else:
            link_poses = forward_kinematics_pt(joint_values, robot_model=self)
        if root_poses is not None:
            return torch.matmul(root_poses.unsqueeze(-3), link_poses)
        return link_poses

    def apply_mimic_joints_numpy(
        self, joint_values: Float[np.ndarray, "*b num_dofs"]
    ) -> Float[np.ndarray, "*b num_joints"]:
        if not self.has_mimic_joints:
            return joint_values
        else:
            mimic_joint_values = joint_values[..., self._mimic_joint_indices_np]
            mimic_joint_values = mimic_joint_values * self._mimic_multipliers_np + self._mimic_offsets_np
            joint_values = np.concatenate([joint_values, mimic_joint_values], axis=-1)
            return joint_values

    def forward_kinematics_numpy(
        self,
        joint_values: Float[np.ndarray, "*b num_dofs"],
        joint_names: Optional[List[str]] = None,
        root_poses: Optional[Float[np.ndarray, "*b 4 4"]] = None,
        clamp_joint_values: bool = True,
    ) -> Float[np.ndarray, "*b num_links 4 4"]:
        """Forward kinematics.

        Args:
            joint_values (np.ndarray): Joint values of shape (batch_size, num_dofs).
            joint_names (list of str, optional): Joint names. Defaults to None.
            root_poses (np.ndarray, optional): Root poses of shape (batch_size, 4, 4). Defaults to None.
            clamp_joint_values (bool, optional): Whether to clamp joint values to joint limits. Defaults to True.
        """
        if joint_names is not None:
            joint_reindex = [joint_names.index(joint_name) for joint_name in self.active_joint_names]
            joint_values = joint_values[:, joint_reindex]
        if clamp_joint_values and self._joint_limits_np is not None:
            joint_values = np.clip(joint_values, self._joint_limits_np[:, 0], self._joint_limits_np[:, 1])
        if self.has_mimic_joints:
            joint_values = self.apply_mimic_joints_numpy(joint_values)
        link_poses = forward_kinematics_wp_np(joint_values, robot_model=self)
        if root_poses is not None:
            return np.matmul(np.expand_dims(root_poses, -3), link_poses)
        return link_poses

    @overload
    def get_zero_joint_values(self, return_tensors: Literal["np"]) -> np.ndarray: ...
    @overload
    def get_zero_joint_values(self, return_tensors: Literal["pt"]) -> torch.Tensor: ...
    def get_zero_joint_values(self, return_tensors: Literal["np", "pt"] = "np") -> Union[np.ndarray, torch.Tensor]:
        if return_tensors == "np":
            return np.zeros((self.num_dofs,), dtype=np.float32)
        elif return_tensors == "pt":
            return torch.zeros((self.num_dofs,), device=self.device, dtype=torch.float32)
        else:
            raise ValueError(f"Unknown return_tensors: {return_tensors}")

    @property
    def zero_joint_values(self) -> torch.Tensor:
        return self.get_zero_joint_values(return_tensors="pt")

    def to(self, device: Device) -> "RobotModel":
        self.config.device = device
        self.device = device

        # clear cached tensors, these tensors will be lazily initialized when accessed
        self._joint_limits_pt = None
        self._joint_axes_pt = None
        self._joint_origins_pt = None
        self._joint_types_pt = None
        self._link_joint_indices_pt = None
        self._link_joint_types_pt = None
        self._link_joint_origins_pt = None
        self._link_indices_topological_order_pt = None
        self._parent_link_indices_pt = None

        return self

    def __repr__(self) -> str:
        result = f"RobotModel(num_dofs={self.num_dofs}, num_links={self.num_links})\n"

        def _chain_str(link_name: str, indent: str = "") -> str:
            chain_str = f"{link_name}"
            indent += " " * len(link_name)
            first_child_joint = True
            for joint_name, joint in self.joint_map.items():
                if joint.parent_link_name == link_name:
                    if not first_child_joint:
                        chain_str += "\n" + indent
                    chain_str += f" -> {_chain_str(joint.child_link_name, indent + '    ')}"
                    first_child_joint = False
            return chain_str

        result += _chain_str(self.base_link_name)
        return result

    def __str__(self) -> str:
        return self.__repr__()


__all__ = ["RobotModelConfig", "RobotModel"]
