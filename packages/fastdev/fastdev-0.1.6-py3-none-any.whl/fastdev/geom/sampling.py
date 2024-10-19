from typing import Optional

import numpy as np
import torch
from jaxtyping import Float, Int64

from fastdev.extension import FDEV_EXT

try:
    import fpsample

    FPSAMPLE_AVAILABLE = True
except ImportError:
    FPSAMPLE_AVAILABLE = False


# TODO: modify the function signature based on pytorch3d's implementation
def sample_farthest_points(
    points: Float[torch.Tensor, "*B N 3"], num_samples: int, random_start: bool = False
) -> Int64[torch.Tensor, "*B num_samples"]:
    """Sample farthest points.

    Args:
        points (Tensor): input points in shape (B, N, 3) or (N, 3)
        num_samples (int): number of samples

    Returns:
        Tensor: indices of farthest points in shape (B, num_samples) or (num_samples,)
    """
    if points.ndim != 2 and points.ndim != 3 or points.shape[-1] != 3:
        raise ValueError("points should be in shape (B, N, 3) or (N, 3).")

    is_batch_input = points.dim() == 3
    if not is_batch_input:
        points = points.unsqueeze(0)

    if random_start:
        start_idx = torch.randint(points.shape[1], (points.shape[0],), device=points.device)
    else:
        start_idx = torch.zeros((points.shape[0],), dtype=torch.long, device=points.device)

    indices = FDEV_EXT.load_module("fastdev_sample_farthest_points").sample_farthest_points(
        points,
        torch.full((points.shape[0],), fill_value=points.shape[1], dtype=torch.long, device=points.device),
        torch.full((points.shape[0],), fill_value=num_samples, dtype=torch.long, device=points.device),
        start_idx,
    )

    if not is_batch_input:
        return indices.squeeze(0)
    else:
        return indices


def sample_farthest_points_numpy(
    points: Float[np.ndarray, "N 3"], num_samples: int, start_idx: Optional[int] = None
) -> Int64[np.ndarray, "num_samples"]:  # noqa: F821
    """Sample farthest points using fpsample.

    Args:
        points (np.ndarray): input points in shape (N, 3)
        num_samples (int): number of samples

    Returns:
        np.ndarray: indices of farthest points in shape (num_samples,)
    """
    if not FPSAMPLE_AVAILABLE:
        raise ImportError("fpsample is not available, please install it via `pip install fpsample`.")

    if points.ndim != 2 or points.shape[-1] != 3:
        raise ValueError("points should be in shape (N, 3), no batch support.")

    return fpsample.bucket_fps_kdline_sampling(points, num_samples, h=3, start_idx=start_idx)  # type: ignore


__all__ = ["sample_farthest_points"]
