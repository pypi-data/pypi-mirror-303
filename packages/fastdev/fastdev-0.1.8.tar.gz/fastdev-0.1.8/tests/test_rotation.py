import torch
from fastdev.xform.rotation import euler_angles_to_matrix as euler_angles_to_matrix_pt
from fastdev.xform.warp_rotation import _AXES_SPEC
from fastdev.xform.warp_rotation import euler_angles_to_matrix as euler_angles_to_matrix_wp


def test_euler_angles_to_matrix():
    euler_angles = torch.tensor([1.0, 0.5, 0.1], requires_grad=True)
    rot_mat = euler_angles_to_matrix_pt(euler_angles, axes="sxyz")
    rot_mat.sum().backward()
    expected_rot_mat = torch.tensor([[0.8732, 0.3475, 0.3417], [0.0876, 0.5779, -0.8114], [-0.4794, 0.7385, 0.4742]])
    expected_grad = torch.tensor([-1.6593, -0.7373, 1.7083])
    assert torch.allclose(rot_mat, expected_rot_mat, atol=1e-4)
    assert torch.allclose(euler_angles.grad, expected_grad, atol=1e-4)

    euler_angles = torch.tensor([1.0, 0.5, 0.1], requires_grad=True)
    rot_mat = euler_angles_to_matrix_wp(euler_angles, axes="sxyz")
    rot_mat.sum().backward()
    assert torch.allclose(rot_mat, expected_rot_mat, atol=1e-4)
    assert torch.allclose(euler_angles.grad, expected_grad, atol=1e-4)

    euler_angles = torch.tensor([1.0, 0.5, 0.1], requires_grad=True)
    rot_mat = euler_angles_to_matrix_pt(euler_angles, axes="rxyz")
    rot_mat.sum().backward()
    expected_rot_mat = torch.tensor([[0.8732, -0.0876, 0.4794], [0.4553, 0.4973, -0.7385], [-0.1737, 0.8631, 0.4742]])
    expected_grad = torch.tensor([-0.9493, 0.8294, 0.1180])
    assert torch.allclose(rot_mat, expected_rot_mat, atol=1e-4)
    assert torch.allclose(euler_angles.grad, expected_grad, atol=1e-4)

    euler_angles = torch.tensor([1.0, 0.5, 0.1], requires_grad=True)
    rot_mat = euler_angles_to_matrix_wp(euler_angles, axes="rxyz")
    rot_mat.sum().backward()
    assert torch.allclose(rot_mat, expected_rot_mat, atol=1e-4)
    assert torch.allclose(euler_angles.grad, expected_grad, atol=1e-4)

    euler_angles = torch.tensor([1.0, 0.5, 0.1], requires_grad=True)
    rot_mat = euler_angles_to_matrix_pt(euler_angles, axes="rzxz")
    rot_mat.sum().backward()
    expected_rot_mat = torch.tensor([[0.4639, -0.7887, 0.4034], [0.8846, 0.3878, -0.2590], [0.0479, 0.4770, 0.8776]])
    expected_grad = torch.tensor([-0.9348, 0.9038, -1.3202])
    assert torch.allclose(rot_mat, expected_rot_mat, atol=1e-4)
    assert torch.allclose(euler_angles.grad, expected_grad, atol=1e-4)

    euler_angles = torch.tensor([1.0, 0.5, 0.1], requires_grad=True)
    rot_mat = euler_angles_to_matrix_wp(euler_angles, axes="rzxz")
    rot_mat.sum().backward()
    assert torch.allclose(rot_mat, expected_rot_mat, atol=1e-4)
    assert torch.allclose(euler_angles.grad, expected_grad, atol=1e-4)


def test_euler_angles_to_matrix_via_transforms3d():
    try:
        from transforms3d.euler import euler2mat
    except ImportError:
        return

    euler_angles = torch.tensor([1.0, 0.5, 0.1])
    for axes in _AXES_SPEC:
        mat = euler2mat(*euler_angles, axes=axes).astype("float32")
        mat1 = euler_angles_to_matrix_pt(euler_angles, axes=axes)
        mat2 = euler_angles_to_matrix_wp(euler_angles, axes=axes)

        assert torch.allclose(mat1, torch.from_numpy(mat), atol=1e-4)
        assert torch.allclose(mat2, torch.from_numpy(mat), atol=1e-4)
