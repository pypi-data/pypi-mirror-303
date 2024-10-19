import torch
import trimesh
from fastdev.geom.warp_meshes import WarpMeshes
from fastdev.xform.rotation import euler_angles_to_matrix
from fastdev.xform.transforms import rot_tl_to_tf_mat


def test_query_signed_distances():
    box = trimesh.creation.box((1.0, 1.0, 1.0))
    meshes = WarpMeshes.from_trimesh_meshes([box], meshes_first_idx=torch.tensor([0]), device="cpu")
    query_pts = torch.tensor([[1.0, 0.0, 0.0], [0.1, 0.0, 0.0]])
    sdf, normals, pts = meshes.query_signed_distances(query_pts, query_points_first_idx=torch.tensor([0]))
    assert torch.allclose(pts, torch.tensor([[0.5, 0.0, 0.0], [0.5, 0.0, 0.0]]))
    assert torch.allclose(normals, torch.tensor([[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]))
    assert torch.allclose(sdf, torch.tensor([0.5, -0.4]))

    mesh_scales = torch.tensor([0.5], device="cpu")
    sdf, normals, pts = meshes.query_signed_distances(
        query_pts, query_points_first_idx=torch.tensor([0]), mesh_scales=mesh_scales
    )
    assert torch.allclose(pts, torch.tensor([[0.25, 0.0, 0.0], [0.25, 0.0, 0.0]]))
    assert torch.allclose(normals, torch.tensor([[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]))
    assert torch.allclose(sdf, torch.tensor([0.75, -0.15]))

    box1 = trimesh.creation.box((1.0, 1.0, 1.0))
    box2 = trimesh.creation.box((1.0, 1.0, 1.0))
    box2.apply_translation([1.3, 0.0, 0.0])
    meshes = WarpMeshes.from_trimesh_meshes([box1, box2], meshes_first_idx=torch.tensor([0]), device="cpu")
    query_pts = torch.tensor([[1.0, 0.0, 0.0], [0.6, 0.0, 0.0]])
    sdf, normals, pts = meshes.query_signed_distances(query_pts, query_points_first_idx=torch.tensor([0]))
    assert torch.allclose(pts, torch.tensor([[0.8, 0.0, 0.0], [0.5, 0.0, 0.0]]))
    assert torch.allclose(normals, torch.tensor([[-1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]))
    assert torch.allclose(sdf, torch.tensor([-0.2, 0.1]))

    mesh_poses = torch.eye(4).unsqueeze(0).repeat(2, 1, 1)
    mesh_poses[..., 0, 3] = 0.2
    sdf, normals, pts = meshes.query_signed_distances(
        query_pts, query_points_first_idx=torch.tensor([0]), mesh_poses=mesh_poses
    )
    assert torch.allclose(pts, torch.tensor([[1.0, 0.0, 0.0], [0.7, 0.0, 0.0]]))
    assert torch.allclose(normals, torch.tensor([[-1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]))
    assert torch.allclose(sdf, torch.tensor([0.0, -0.1]))


def test_query_signed_distances_grad():
    device = "cpu"
    box = trimesh.creation.box((1, 1, 1))
    meshes = WarpMeshes.from_trimesh_meshes([box], meshes_first_idx=torch.tensor([0]), device="cpu")
    pts = torch.tensor(
        [
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.5],
            [1.0, 1.0, 1.0],
            [1.5, 1.5, 1.5],
        ],
        dtype=torch.float32,
        device=device,
        requires_grad=True,
    )
    sdf, normals, clse_pts = meshes.query_signed_distances(pts, torch.tensor([0]))
    sdf.abs().sum().backward()
    assert torch.allclose(
        pts.grad,
        torch.tensor(
            [[-1.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000], [0.5774, 0.5774, 0.5774], [0.5774, 0.5774, 0.5774]],
            device=device,
        ),
        atol=1e-4,
    )

    pts.grad.zero_()
    pose = rot_tl_to_tf_mat(euler_angles_to_matrix(torch.tensor([0.1, 0.2, 0.3])), torch.tensor([-0.1, -0.1, -0.1]))
    pose.requires_grad_(True)
    sdf, normals, clse_pts = meshes.query_signed_distances(pts, torch.tensor([0]), mesh_poses=pose.unsqueeze(0))
    sdf.sum().backward()
    assert torch.allclose(
        pts.grad,
        torch.tensor(
            [[0.2184, -0.0370, 0.9752], [0.6689, 0.1173, 0.7340], [0.6237, 0.4680, 0.6261], [0.6041, 0.5183, 0.6054]],
            device=device,
        ),
        atol=1e-4,
    )
    assert torch.allclose(
        pose.grad,
        torch.tensor(
            [
                [1.9159, 0.9930, 2.5419, -2.1150],
                [1.9159, 0.9930, 2.5419, -1.0666],
                [1.9159, 0.9930, 2.5419, -2.9407],
                [0.0000, 0.0000, 0.0000, 0.0000],
            ],
            device=device,
        ),
        atol=1e-4,
    )


def test_query_signed_distances_multi_scenes():
    box1 = trimesh.creation.box((1.0, 1.0, 1.0))
    box2 = trimesh.creation.box((0.5, 0.5, 10.0))
    box3 = trimesh.creation.box((0.3, 0.3, 0.3))
    box4 = trimesh.creation.box((0.2, 0.2, 10.0))
    box5 = trimesh.creation.box((0.1, 0.1, 20.0))
    meshes = WarpMeshes.from_trimesh_meshes(
        [box1, box2, box3, box4, box5], meshes_first_idx=torch.tensor([0, 2]), device="cpu"
    )
    query_pts = torch.tensor([[1.0, 0.0, 0.0], [0.3, 0.0, 5.0], [0.3, 0.0, 0.0], [0.11, 0.0, 5.0], [0.06, 0.0, 10.0]])
    sdf, normals, pts = meshes.query_signed_distances(query_pts, query_points_first_idx=torch.tensor([0, 2]))
    assert torch.allclose(
        pts, torch.tensor([[0.5, 0.0, 0.0], [0.25, 0.0, 5.0], [0.15, 0.0, 0.0], [0.1, 0.0, 5.0], [0.05, 0.0, 10.0]])
    )
    assert torch.allclose(
        normals, torch.tensor([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])
    )
    assert torch.allclose(sdf, torch.tensor([0.5000, 0.0500, 0.1500, 0.0100, 0.0100]))
