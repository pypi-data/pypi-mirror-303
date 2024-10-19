import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Counter as CounterT
from typing import Dict, List, cast

import numpy as np
import sapien.physx as physx
import trimesh
import trimesh.creation
from gymnasium import Env
from mani_skill.envs.scene import ManiSkillScene
from mani_skill.utils.geometry.trimesh_utils import merge_meshes
from sapien.physx import PhysxRigidBaseComponent

from fastdev.sim_webui.webui import (
    ASSET_LIBRARY,
    IS_PLAYING_EVENT,
    Color,
    MeshAsset,
    SimWebUI,
    StateManager,
    ViserAssetState,
    ViserHelper,
    get_random_color,
    to_color_array,
    to_position_wxyz,
)
from fastdev.utils.profile_utils import timeit
from fastdev.utils.tensor_utils import to_numpy
from fastdev.utils.tui_utils import log_once


# NOTE somehow `get_component_meshes` from `mani_skill.utils.geometry.trimesh_utils` is not correct
def get_component_meshes(component: physx.PhysxRigidBaseComponent):
    """Get component (collision) meshes in the component's frame."""
    meshes = []
    for geom in component.get_collision_shapes():
        if isinstance(geom, physx.PhysxCollisionShapeBox):
            mesh = trimesh.creation.box(extents=2 * geom.half_size)
        elif isinstance(geom, physx.PhysxCollisionShapeCapsule):
            extra_trimesh_tf_mat = np.array([[0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]], dtype=np.float32)
            mesh = trimesh.creation.capsule(
                radius=geom.radius, height=2 * geom.half_length, transform=extra_trimesh_tf_mat
            )
        elif isinstance(geom, physx.PhysxCollisionShapeCylinder):
            extra_trimesh_tf_mat = np.array([[0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]], dtype=np.float32)
            mesh = trimesh.creation.cylinder(
                radius=geom.radius, height=2 * geom.half_length, transform=extra_trimesh_tf_mat
            )
        elif isinstance(geom, physx.PhysxCollisionShapeSphere):
            mesh = trimesh.creation.icosphere(radius=geom.radius)
        elif isinstance(geom, physx.PhysxCollisionShapePlane):
            continue
        elif isinstance(geom, (physx.PhysxCollisionShapeConvexMesh)):
            vertices = geom.vertices  # [n, 3]
            faces = geom.get_triangles()
            vertices = vertices * geom.scale
            mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
        elif isinstance(geom, physx.PhysxCollisionShapeTriangleMesh):
            vertices = geom.vertices
            faces = geom.get_triangles()
            vertices = vertices * geom.scale
            mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
        else:
            raise TypeError(type(geom))
        mesh.apply_transform(geom.get_local_pose().to_transformation_matrix())
        meshes.append(mesh)
    return meshes


@dataclass
class ManiSkillStateManger(StateManager):
    _num_scenes: int = 0
    _scene_last_updated: float = field(default_factory=time.time)

    component_poses_history: List[Dict[str, np.ndarray]] = field(default_factory=list)
    component_colors: Dict[str, Color] = field(default_factory=dict)
    component_name_to_asset_id: Dict[str, str] = field(default_factory=dict)
    component_name_to_scene_indices: Dict[str, List[int]] = field(default_factory=lambda: defaultdict(list))
    scene_index_to_component_names: Dict[int, List[str]] = field(default_factory=lambda: defaultdict(list))

    def get_scene_num_frames(self, scene_index: int) -> int:
        return len(self.component_poses_history)

    @lru_cache(maxsize=256)
    def get_frame_viser_asset_states(self, scene_index: int, frame_index: int) -> List[ViserAssetState]:
        if frame_index >= len(self.component_poses_history):
            return []
        viser_asset_states: List[ViserAssetState] = []
        asset_ids: CounterT[str] = Counter()
        for component_name in self.scene_index_to_component_names[scene_index]:
            asset_id = self.component_name_to_asset_id[component_name]
            data_offset = self.component_name_to_scene_indices[component_name].index(scene_index)
            pose = self.component_poses_history[frame_index][component_name][data_offset]
            asset_id = self.component_name_to_asset_id[component_name]
            mesh_asset: MeshAsset = cast(MeshAsset, ASSET_LIBRARY.get_asset(asset_id))
            pos, wxyz = to_position_wxyz(pose)
            color = self.component_colors.get(component_name, to_color_array("silver"))
            viser_asset_state = ViserAssetState(
                asset_id=asset_id,
                viser_asset_id=mesh_asset.get_or_create_asset_id(color, 1.0, postfix=asset_ids[asset_id]),
                position=pos,
                wxyz=wxyz,
            )
            viser_asset_states.append(viser_asset_state)
            asset_ids[asset_id] += 1
        return viser_asset_states

    @property
    def num_scenes(self) -> int:
        return self._num_scenes

    @num_scenes.setter
    def num_scenes(self, num_scenes: int):
        self._num_scenes = num_scenes

    def get_scene_last_updated(self, scene_index: int) -> float:
        return self._scene_last_updated

    def reset(self):
        self.component_poses_history = []
        self.component_name_to_asset_id = {}
        self.component_colors = {}
        self.component_name_to_scene_indices = defaultdict(list)
        self.scene_index_to_component_names = defaultdict(list)
        self._scene_last_updated = time.time()
        self.get_frame_viser_asset_states.cache_clear()

    def set_robot_state(self, *args, **kwargs):
        raise ValueError("set_robot_state is not supported in ManiSkillStateManger")

    def set_mesh_state(self, *args, **kwargs):
        raise ValueError("set_mesh_state is not supported in ManiSkillStateManger")

    def set_point_cloud_state(self, *args, **kwargs):
        raise ValueError("set_point_cloud_state is not supported in ManiSkillStateManger")

    def __getitem__(self, scene_index: int):
        raise ValueError("ManiSkillStateManger does not support __getitem__")

    def __hash__(self) -> int:
        return hash((self._num_scenes, self._scene_last_updated))

    def __repr__(self) -> str:
        return f"ManiSkillStateManger(num_scenes={self._num_scenes})"

    def __str__(self) -> str:
        return self.__repr__()


class ManiSkillWebUI(SimWebUI):
    def __init__(self, env: Env, host: str = "localhost", port: int = 8080, disable_cache: bool = False):
        self._state_manager = ManiSkillStateManger()
        self._viser_helper = ViserHelper(
            state_manager=self._state_manager,
            host=host,
            port=port,
            enable_geometry_option=False,
        )
        self._disable_cache = disable_cache

        if not isinstance(env, Env):
            raise ValueError(f"env must be an instance of gymnasium.Env, got {type(env)}")
        if not isinstance(env.unwrapped.scene, ManiSkillScene):  # type: ignore
            raise ValueError(f"env must have a scene of type ManiSkillScene, got {type(env.unwrapped.scene)}")  # type: ignore

        self._env: Env = env
        self._state_manager.num_scenes = self._env.unwrapped.num_envs  # type: ignore

        # get assets and poses from the simulation
        self._get_assets_from_sim()
        self._get_asset_poses_from_sim()

        # override step function
        self._override_step()
        self._override_reset()

        # update the viser server
        self._viser_helper.update_server()

    def _override_step(self):
        ori_step_fn = self._env.step

        def step_fn(*args, **kwargs):
            log_once("The simulation will be paused if the web UI is not playing")
            IS_PLAYING_EVENT.wait()

            ori_ret = ori_step_fn(*args, **kwargs)
            self._get_asset_poses_from_sim()
            self._viser_helper.update_server()
            return ori_ret

        # monkeypatch the step function
        self._env.step = step_fn

    def _override_reset(self):
        ori_reset_fn = self._env.reset

        def reset_fn(*args, **kwargs):
            ori_ret = ori_reset_fn(*args, **kwargs)
            self._state_manager.reset()
            self._viser_helper.reset()
            self._get_assets_from_sim()
            self._get_asset_poses_from_sim()
            self._viser_helper.update_server()
            return ori_ret

        # monkeypatch the reset function in sapien
        self._env.reset = reset_fn

    @timeit("ManiSkillWebUI.get_assets_from_sim")
    def _get_assets_from_sim(self):
        scene: ManiSkillScene = self._env.unwrapped.scene  # type: ignore

        # add robots
        for arti_name, articulation in scene.articulations.items():
            art_scene_idxs = articulation._scene_idxs.tolist()
            for link_name, link in articulation.links_map.items():
                # it manages multiple sapien articulation objects, we only need the first one
                link_mesh = merge_meshes(get_component_meshes(link._objs[0]))
                if link_mesh is None:
                    continue
                component_name = f"arti_{arti_name}/{link_name}"
                asset_id = self.add_mesh_asset(trimesh_mesh=link_mesh, disable_cache=self._disable_cache)

                self._state_manager.component_name_to_asset_id[component_name] = asset_id
                self._state_manager.component_colors[component_name] = to_color_array("silver")
                self._state_manager.component_name_to_scene_indices[component_name] = art_scene_idxs
                for scene_idx in art_scene_idxs:
                    self._state_manager.scene_index_to_component_names[scene_idx].append(component_name)

        # add objects
        for actor_name, actor in scene.actors.items():
            act_scene_idxs = actor._scene_idxs.tolist()
            component_name = f"actor_{actor_name}"
            act = actor._objs[0]
            act_meshes = []
            for comp in act.components:
                if isinstance(comp, PhysxRigidBaseComponent):
                    comp_mesh = merge_meshes(get_component_meshes(comp))
                    if comp_mesh is not None:
                        act_meshes.append(comp_mesh)
            if len(act_meshes) == 0:
                continue
            asset_id = self.add_mesh_asset(trimesh_mesh=merge_meshes(act_meshes), disable_cache=self._disable_cache)
            self._state_manager.component_name_to_asset_id[component_name] = asset_id
            self._state_manager.component_colors[component_name] = get_random_color()
            self._state_manager.component_name_to_scene_indices[component_name] = act_scene_idxs
            for scene_idx in act_scene_idxs:
                self._state_manager.scene_index_to_component_names[scene_idx].append(component_name)

    def _get_asset_poses_from_sim(self):
        scene: ManiSkillScene = self._env.unwrapped.scene  # type: ignore

        component_poses = {}
        for arti_name, articulation in scene.articulations.items():
            for link_name, link in articulation.links_map.items():
                component_name = f"arti_{arti_name}/{link_name}"
                if component_name not in self._state_manager.component_name_to_asset_id:
                    continue
                link_pose = to_numpy(link.pose.raw_pose)
                component_poses[component_name] = link_pose

        for actor_name, actor in scene.actors.items():
            component_name = f"actor_{actor_name}"
            actor_pose = to_numpy(actor.pose.raw_pose)
            component_poses[component_name] = actor_pose

        self._state_manager.component_poses_history.append(component_poses)

    def set_robot_state(self, *args, **kwargs):
        raise ValueError("set_robot_state is not supported in ManiSkillWebUI")

    def set_mesh_state(self, *args, **kwargs):
        raise ValueError("set_mesh_state is not supported in ManiSkillWebUI")

    def set_point_cloud_state(self, *args, **kwargs):
        raise ValueError("set_point_cloud_state is not supported in ManiSkillWebUI")

    def __repr__(self) -> str:
        return f"ManiSkillWebUI(num_scenes={self._state_manager.num_scenes})"

    def __str__(self) -> str:
        return self.__repr__()
