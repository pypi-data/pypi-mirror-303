import numpy as np
import trimesh
from fastdev.sim_webui.webui import SimWebUI


def test_webui():
    webui = SimWebUI()
    asset_id = webui.add_robot_asset("assets/robot_description/panda.urdf")
    asset_id_1 = webui.add_robot_asset("assets/robot_description/panda.urdf")
    assert asset_id == asset_id_1
    joint_values = np.zeros((10, 8))
    joint_values[:, -1] = np.linspace(0, 0.05, 10)
    webui.set_robot_state(asset_id, scene_index=0, color="silver", joint_values=joint_values)
    webui.set_robot_state(asset_id, scene_index=1, color="black")

    assert webui._state_manager.get_scene_num_frames(scene_index=0) == 10
    assert webui._state_manager.get_scene_num_frames(scene_index=1) == 1
    assert (
        "#c0c0c0" in webui._state_manager.get_frame_viser_asset_states(scene_index=0, frame_index=0)[-1].viser_asset_id
    )
    assert np.allclose(
        np.array([1.03232495e-01, -1.29130821e-12, 8.66684139e-01], dtype=np.float32),
        webui._state_manager.get_frame_viser_asset_states(scene_index=0, frame_index=0)[-1].position,
    )

    box_mesh = trimesh.creation.box((0.5, 0.5, 0.2))
    box_mesh.vertices -= np.array([0, 0, 0.1])
    mesh_asset_id = webui.add_mesh_asset(trimesh_mesh=box_mesh)
    mesh_asset_id_1 = webui.add_mesh_asset(trimesh_mesh=box_mesh)
    assert mesh_asset_id == mesh_asset_id_1
    webui.set_mesh_state(mesh_asset_id, scene_index=0)
    assert webui._state_manager[0]._mesh_states[mesh_asset_id].scale == 1.0

    pc = np.random.rand(1024, 3)
    pc_asset_id = webui.add_point_cloud_asset(pc)
    webui.set_point_cloud_state(pc_asset_id, scene_index=0)
    webui.set_point_cloud_state(pc_asset_id, scene_index=0, point_size=0.01, poses=np.eye(4)[None].repeat(10, axis=0))
    assert webui._state_manager[0]._pc_states[pc_asset_id].point_size == 0.01


def test_webui_frames():
    webui = SimWebUI()
    pc = np.random.rand(1024, 3)
    pc_asset_id = webui.add_point_cloud_asset(pc)
    webui.set_point_cloud_state(pc_asset_id, scene_index=0)
    assert webui._state_manager.get_scene_num_frames(scene_index=0) == 1
    webui.set_point_cloud_state(pc_asset_id, scene_index=0, point_size=0.01, poses=np.eye(4)[None].repeat(10, axis=0))
    assert webui._state_manager.get_scene_num_frames(scene_index=0) == 10
    webui.set_point_cloud_state(pc_asset_id, scene_index=0)
    assert webui._state_manager.get_scene_num_frames(scene_index=0) == 10
    webui.reset()
    assert webui._state_manager.get_scene_num_frames(scene_index=0) == 0
