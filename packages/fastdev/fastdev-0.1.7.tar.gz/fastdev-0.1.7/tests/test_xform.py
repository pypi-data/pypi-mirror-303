import torch
from packaging.version import Version


def test_transform_points():
    from fastdev.xform.transforms import transform_points

    pts = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=torch.float32)
    tf_mat = torch.tensor(
        [[0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 2.0], [1.0, 0.0, 0.0, 3.0], [0.0, 0.0, 0.0, 1.0]], dtype=torch.float32
    )
    new_pts = transform_points(pts, tf_mat)
    tgt_pts = torch.tensor([[3.0, 5.0, 4.0], [6.0, 8.0, 7.0]], dtype=torch.float32)
    assert torch.allclose(new_pts, tgt_pts)

    new_pts = transform_points(pts[None], tf_mat[None])[0]
    assert torch.allclose(new_pts, tgt_pts)

    dtype = torch.float16 if Version(torch.__version__) > Version("2.0.0") else torch.float64
    new_pts = transform_points(pts.to(dtype=dtype), tf_mat.to(dtype=dtype))
    assert torch.allclose(new_pts, tgt_pts.to(dtype=dtype))
    assert new_pts.dtype == dtype


def test_transform_points_warp():
    from fastdev.xform.warp_transforms import transform_points

    pts = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=torch.float32, requires_grad=True)
    tf_mat = torch.tensor(
        [[0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 2.0], [1.0, 0.0, 0.0, 3.0], [0.0, 0.0, 0.0, 1.0]], dtype=torch.float32
    )
    new_pts = transform_points(pts, tf_mat)
    new_pts[:-1].sum().backward()
    tgt_pts = torch.tensor([[3.0, 5.0, 4.0], [6.0, 8.0, 7.0]], dtype=torch.float32)
    assert torch.allclose(new_pts, tgt_pts)
    assert torch.allclose(pts.grad, torch.tensor([[1.0, 1.0, 1.0], [0.0, 0.0, 0.0]]))  # type: ignore

    new_pts = transform_points(pts[None], tf_mat[None])[0]
    assert torch.allclose(new_pts, tgt_pts)

    pts = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=torch.float32)
    tf_mat = torch.tensor(
        [[0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 2.0], [1.0, 0.0, 0.0, 3.0], [0.0, 0.0, 0.0, 1.0]],
        dtype=torch.float32,
        requires_grad=True,
    )
    new_pts = transform_points(pts, tf_mat)
    new_pts[:-1].sum().backward()
    assert torch.allclose(
        tf_mat.grad,  # type: ignore
        torch.tensor([[1.0, 2.0, 3.0, 1.0], [1.0, 2.0, 3.0, 1.0], [1.0, 2.0, 3.0, 1.0], [0.0, 0.0, 0.0, 0.0]]),
    )


def test_rotate_points_warp():
    from fastdev.xform.warp_transforms import rotate_points

    pts = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=torch.float32, requires_grad=True)
    rot_mat = torch.tensor(
        [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]],
        dtype=torch.float32,
        requires_grad=True,
    )
    new_pts = rotate_points(pts, rot_mat)
    new_pts[:-1].sum().backward()

    tgt_pts = torch.tensor([[2.0, 3.0, 1.0], [5.0, 6.0, 4.0]], dtype=torch.float32)
    torch.allclose(new_pts, tgt_pts)
    assert torch.allclose(pts.grad, torch.tensor([[1.0, 1.0, 1.0], [0.0, 0.0, 0.0]]))  # type: ignore


def test_axis_angle_to_matrix_warp():
    from fastdev.xform.warp_rotation import axis_angle_to_matrix

    axis = torch.tensor([1.0, 0.0, 0.0], requires_grad=True)
    angle = torch.tensor(0.5)
    rot_mat = axis_angle_to_matrix(axis, angle)
    tgt_rot_mat = torch.tensor(
        [[1.0, 0.0, 0.0], [0.0, 0.87758255, -0.47942555], [0.0, 0.47942555, 0.87758255]], dtype=torch.float32
    )
    assert torch.allclose(rot_mat, tgt_rot_mat, atol=1e-5)
    rot_mat.sum().backward()
    assert torch.allclose(axis.grad, torch.tensor([0.2448, 0.2448, 0.2448]), atol=1e-4)  # type: ignore

    rot_mat = axis_angle_to_matrix(axis[None], angle[None])[0]
    assert torch.allclose(rot_mat, tgt_rot_mat)
