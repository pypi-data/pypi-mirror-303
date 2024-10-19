import numpy as np
import torch
from fastdev.utils.tensor_utils import auto_cast, to_numpy, to_torch
from jaxtyping import Float


def test_to_numpy():
    a = torch.tensor([1, 2, 3], dtype=torch.float32)
    b = np.array([1, 2, 3])
    assert np.allclose(to_numpy(a), b)

    a.requires_grad_()
    assert np.allclose(to_numpy(a), b)

    if torch.cuda.is_available():
        a = torch.tensor([1, 2, 3]).cuda()
        assert np.allclose(to_numpy(a), b)

    a = {"a": torch.tensor([1, 2, 3], dtype=torch.float32)}
    assert np.allclose(to_numpy(a)["a"], b)

    a = [torch.tensor([1, 2, 3], dtype=torch.float32)]
    assert np.allclose(to_numpy(a)[0], b)

    a = (torch.tensor([1, 2, 3], dtype=torch.float32),)
    assert np.allclose(to_numpy(a)[0], b)

    a = [1, 2, 3]
    assert np.allclose(to_numpy(a, preserve_list=False), b)


def test_to_torch():
    a = np.array([1, 2, 3], dtype=np.float32)
    b = torch.tensor([1, 2, 3], dtype=torch.float32)
    assert torch.allclose(to_torch(a), b)

    a = {"a": np.array([1, 2, 3], dtype=np.float32)}
    assert torch.allclose(to_torch(a)["a"], b)

    a = [np.array([1, 2, 3], dtype=np.float32)]
    assert torch.allclose(to_torch(a)[0], b)

    a = (np.array([1, 2, 3], dtype=np.float32),)
    assert torch.allclose(to_torch(a)[0], b)

    a = [1.0, 2.0, 3.0]
    assert torch.allclose(to_torch(a, preserve_list=False), b)


def test_auto_cast():
    def f1(x: torch.Tensor) -> torch.Tensor:
        return torch.cos(x)

    x_pt = torch.tensor([0.0, 1.0, 2.0])
    x_np = to_numpy(x_pt)

    y_pt = f1(x_pt)
    y_np = auto_cast(f1)(x_np)
    assert np.allclose(to_numpy(y_pt), y_np)

    @auto_cast
    def f2(x: np.ndarray) -> np.ndarray:
        return np.cos(x)

    y_pt = f2(x_pt)
    assert np.allclose(to_numpy(y_pt), np.cos(x_np))

    @auto_cast(return_type="pt")
    def f3(x: np.ndarray) -> np.ndarray:
        return np.cos(x)

    y_pt = f3(x_np)
    assert np.allclose(to_numpy(y_pt), np.cos(x_np))

    @auto_cast(return_type="pt")
    def f4(x: np.ndarray):
        return np.cos(x), np.sin(x)

    y_pt = f4(x_np)
    assert np.allclose(to_numpy(y_pt[0]), np.cos(x_np))
    assert np.allclose(to_numpy(y_pt[1]), np.sin(x_np))

    y_pt = f4(x_pt)  # type: ignore
    assert np.allclose(to_numpy(y_pt[0]), np.cos(x_np))
    assert np.allclose(to_numpy(y_pt[1]), np.sin(x_np))

    @auto_cast(return_type="pt")
    def f5(x: Float[np.ndarray, "..."]) -> Float[np.ndarray, "..."]:
        return np.cos(x)

    y_pt = f5(x_pt)  # type: ignore
    assert np.allclose(to_numpy(y_pt), np.cos(x_np))


if __name__ == "__main__":
    test_auto_cast()
