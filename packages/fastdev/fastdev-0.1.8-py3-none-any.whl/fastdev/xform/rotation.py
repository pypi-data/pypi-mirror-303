from typing import Dict, Literal, Optional, Union, get_args

import numpy as np
import torch
import torch.nn.functional as F
from jaxtyping import Float
from torch import Tensor


def random_rotation_matrix(
    num: Optional[int] = None,
    random_state: Optional[Union[int, np.random.Generator, np.random.RandomState]] = None,
    return_tensors: Literal["np", "pt"] = "np",
):
    try:
        from scipy.spatial.transform import Rotation as R
    except ImportError:
        raise ImportError("This function requires scipy to be installed.")

    random_rotations = R.random(num=num, random_state=random_state)

    rotation_matrices = random_rotations.as_matrix()

    if return_tensors == "pt":
        return torch.as_tensor(rotation_matrices, dtype=torch.float32)
    elif return_tensors == "np":
        return rotation_matrices
    else:
        raise ValueError("return_tensors should be either 'np' or 'pt'")


# Adapted from https://github.com/facebookresearch/pytorch3d/blob/main/pytorch3d/transforms/rotation_conversions.py
def _sqrt_positive_part(x: torch.Tensor) -> torch.Tensor:
    ret = torch.zeros_like(x)
    positive_mask = x > 0
    ret[positive_mask] = torch.sqrt(x[positive_mask])
    return ret


def split_axis_angle_vector(axis_angle):
    axis_angle = torch.as_tensor(axis_angle)
    angle = torch.norm(axis_angle, p=2, dim=-1, keepdim=True)  # type: ignore
    axis = axis_angle / angle
    return axis, angle


def compose_axis_angle_vector(axis, angle):
    return axis * angle


def axis_angle_vector_to_matrix(axis_angle: torch.Tensor) -> torch.Tensor:
    """
    Convert rotations given as axis/angle to rotation matrices.

    Args:
        axis_angle: Rotations given as a vector in axis angle form,
            as a tensor of shape (..., 3), where the magnitude is
            the angle turned anticlockwise in radians around the
            vector's direction.

    Returns:
        Rotation matrices as tensor of shape (..., 3, 3).
    """
    return quaternion_to_matrix(axis_angle_vector_to_quaternion(axis_angle))


def matrix_to_axis_angle_vector(matrix: torch.Tensor) -> torch.Tensor:
    """
    Convert rotations given as rotation matrices to axis/angle.

    Args:
        matrix: Rotation matrices as tensor of shape (..., 3, 3).

    Returns:
        Rotations given as a vector in axis angle form, as a tensor
            of shape (..., 3), where the magnitude is the angle
            turned anticlockwise in radians around the vector's
            direction.
    """
    return quaternion_to_axis_angle_vector(matrix_to_quaternion(matrix))


def axis_angle_vector_to_quaternion(axis_angle):
    """
    Convert rotations given as axis/angle to quaternions.

    Args:
        axis_angle: Rotations given as a vector in axis angle form,
            as a tensor of shape (..., 3), where the magnitude is
            the angle turned anticlockwise in radians around the
            vector's direction.
    Returns:
        quaternions with real part first, as tensor of shape (..., 4).
    Reference: https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Unit_quaternions
    """
    axis_angle = torch.as_tensor(axis_angle)
    angles = torch.norm(axis_angle, p=2, dim=-1, keepdim=True)  # type: ignore
    half_angles = angles * 0.5
    eps = 1e-6
    small_angles = torch.abs(angles) < eps
    sin_half_angles_over_angles = torch.empty_like(angles)
    sin_half_angles_over_angles[~small_angles] = torch.sin(half_angles[~small_angles]) / angles[~small_angles]
    # for x small, sin(x/2) is about x/2 - (x/2)^3/6
    # so sin(x/2)/x is about 1/2 - (x*x)/48
    sin_half_angles_over_angles[small_angles] = 0.5 - (angles[small_angles] * angles[small_angles]) / 48
    quaternions = torch.cat([torch.cos(half_angles), axis_angle * sin_half_angles_over_angles], dim=-1)
    return quaternions


def quaternion_to_axis_angle_vector(quaternions):
    """
    Convert rotations given as quaternions to axis/angle.

    Args:
        quaternions: quaternions with real part first,
            as tensor of shape (..., 4).
    Returns:
        Rotations given as a vector in axis angle form, as a tensor
            of shape (..., 3), where the magnitude is the angle
            turned anticlockwise in radians around the vector's
            direction.
    Reference: https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Unit_quaternions
    """
    norms = torch.norm(quaternions[..., 1:], p=2, dim=-1, keepdim=True)  # type: ignore
    half_angles = torch.atan2(norms, quaternions[..., :1])
    angles = 2 * half_angles
    eps = 1e-6
    small_angles = torch.abs(angles) < eps
    sin_half_angles_over_angles = torch.empty_like(angles)
    sin_half_angles_over_angles[~small_angles] = torch.sin(half_angles[~small_angles]) / angles[~small_angles]
    # for x small, sin(x/2) is about x/2 - (x/2)^3/6
    # so sin(x/2)/x is about 1/2 - (x*x)/48
    sin_half_angles_over_angles[small_angles] = 0.5 - (angles[small_angles] * angles[small_angles]) / 48
    quaternions = quaternions[..., 1:] / sin_half_angles_over_angles
    return quaternions


def normalize_quaternion(quaternions: torch.Tensor) -> torch.Tensor:
    """
    Normalize quaternions to have unit length.

    Args:
        quaternions: quaternions with real part first,
            as tensor of shape (..., 4).
    Returns:
        Normalized quaternions as tensor of shape (..., 4).
    """
    return F.normalize(quaternions, p=2, dim=-1)


def standardize_quaternion(quaternions: torch.Tensor) -> torch.Tensor:
    """
    Convert a unit quaternion to a standard form: one in which the real
    part is non negative.

    Args:
        quaternions: Quaternions with real part first, as tensor of shape (..., 4).
    Returns:
        Standardized quaternions as tensor of shape (..., 4).
    """
    return torch.where(quaternions[..., 0:1] < 0, -quaternions, quaternions)


def quaternion_real_to_last(quaternions):
    # move the real part in quaternions to last
    return quaternions[..., [1, 2, 3, 0]]


def quaternion_real_to_first(quaternions):
    # move the real part in quaternions to first
    return quaternions[..., [3, 0, 1, 2]]


def quaternion_raw_multiply(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """
    Multiply two quaternions.
    Usual torch rules for broadcasting apply.

    Args:
        a: Quaternions as tensor of shape (..., 4), real part first.
        b: Quaternions as tensor of shape (..., 4), real part first.

    Returns:
        The product of a and b, a tensor of quaternions shape (..., 4).
    """
    aw, ax, ay, az = torch.unbind(a, -1)
    bw, bx, by, bz = torch.unbind(b, -1)  # type: ignore
    ow = aw * bw - ax * bx - ay * by - az * bz
    ox = aw * bx + ax * bw + ay * bz - az * by
    oy = aw * by - ax * bz + ay * bw + az * bx
    oz = aw * bz + ax * by - ay * bx + az * bw
    return torch.stack((ow, ox, oy, oz), -1)


def quaternion_multiply(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """
    Multiply two quaternions representing rotations, returning the quaternion
    representing their composition, i.e. the versor with nonnegative real part.
    Usual torch rules for broadcasting apply.

    Args:
        a: Quaternions as tensor of shape (..., 4), real part first.
        b: Quaternions as tensor of shape (..., 4), real part first.

    Returns:
        The product of a and b, a tensor of quaternions of shape (..., 4).
    """
    ab = quaternion_raw_multiply(a, b)
    return standardize_quaternion(ab)


def quaternion_invert(quaternion: torch.Tensor) -> torch.Tensor:
    """
    Given a quaternion representing rotation, get the quaternion representing
    its inverse.

    Args:
        quaternion: Quaternions as tensor of shape (..., 4), with real part
            first, which must be versors (unit quaternions).

    Returns:
        The inverse, a tensor of quaternions of shape (..., 4).
    """
    scaling = torch.tensor([1, -1, -1, -1], device=quaternion.device)
    return quaternion * scaling


def quaternion_apply(quaternion: torch.Tensor, point: torch.Tensor) -> torch.Tensor:
    """
    Apply the rotation given by a quaternion to a 3D point.
    Usual torch rules for broadcasting apply.

    Args:
        quaternion: Tensor of quaternions, real part first, of shape (..., 4).
        point: Tensor of 3D points of shape (..., 3).

    Returns:
        Tensor of rotated points of shape (..., 3).
    """
    if point.size(-1) != 3:
        raise ValueError(f"Points are not in 3D, {point.shape}.")
    real_parts = point.new_zeros(point.shape[:-1] + (1,))
    point_as_quaternion = torch.cat((real_parts, point), -1)
    out = quaternion_raw_multiply(
        quaternion_raw_multiply(quaternion, point_as_quaternion),
        quaternion_invert(quaternion),
    )
    return out[..., 1:]


def quaternion_to_matrix(quaternions: Tensor) -> Tensor:
    """Convert rotations given as quaternions to rotation matrices.

    Args:
        quaternions (Tensor): quaternions with real part first with shape (..., 4).

    Returns:
        Tensor: Rotation matrices as tensor of shape (..., 3, 3).

    Reference: https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
    """
    r, i, j, k = torch.unbind(quaternions, -1)
    two_s = 2.0 / torch.sum(quaternions * quaternions, dim=-1)
    # fmt: off
    matrices = torch.stack([1 - two_s * (j * j + k * k), two_s * (i * j - k * r), two_s * (i * k + j * r),
                           two_s * (i * j + k * r), 1 - two_s * (i * i + k * k), two_s * (j * k - i * r),
                           two_s * (i * k - j * r), two_s * (j * k + i * r), 1 - two_s * (i * i + j * j)], dim=-1)
    # fmt: on
    matrices = torch.reshape(matrices, quaternions.shape[:-1] + (3, 3))
    return matrices


def matrix_to_quaternion(matrix: Float[torch.Tensor, "... 3 3"]) -> Float[torch.Tensor, "... 4"]:
    """
    Convert rotation matrices to quaternions using Shepperds's method.

    Args:
        matrix: (np.ndarray, torch.Tensor): rotation matrices, the shape could be ...3x3.

    Returns:
        quaternions with real part first in shape of (..., 4).

    Example:
        >>> rot_mat = torch.tensor([[-0.2533, -0.6075,  0.7529],
        ...                         [ 0.8445, -0.5185, -0.1343],
        ...                         [ 0.4720,  0.6017,  0.6443]])
        >>> matrix_to_quaternion(rot_mat)
        tensor([0.4671, 0.3940, 0.1503, 0.7772])

    Ref: http://www.iri.upc.edu/files/scidoc/2068-Accurate-Computation-of-Quaternions-from-Rotation-Matrices.pdf
        Note that the way to determine the best solution is slightly different from the PDF.
    """
    batch_dim = matrix.shape[:-2]
    m00, m01, m02, m10, m11, m12, m20, m21, m22 = torch.unbind(torch.reshape(matrix, batch_dim + (9,)), dim=-1)
    # fmt: off
    q_abs = _sqrt_positive_part(torch.stack([1.0 + m00 + m11 + m22, 1.0 + m00 - m11 - m22,
                                            1.0 - m00 + m11 - m22, 1.0 - m00 - m11 + m22], dim=-1))
    # we produce the desired quaternion multiplied by each of r, i, j, k
    quat_by_rijk = torch.stack([torch.stack([q_abs[..., 0] ** 2, m21 - m12, m02 - m20, m10 - m01], dim=-1),
                               torch.stack([m21 - m12, q_abs[..., 1] ** 2, m10 + m01, m02 + m20], dim=-1),
                               torch.stack([m02 - m20, m10 + m01, q_abs[..., 2] ** 2, m12 + m21], dim=-1),
                               torch.stack([m10 - m01, m20 + m02, m21 + m12, q_abs[..., 3] ** 2], dim=-1)], dim=-2)
    # fmt: on
    # We floor here at 0.1 but the exact level is not important; if q_abs is small, the candidate won't be picked.
    flr = torch.tensor([0.1], device=q_abs.device, dtype=q_abs.dtype)
    quat_candidates = quat_by_rijk / (2.0 * torch.maximum(q_abs[..., None], flr))

    quat = quat_candidates[F.one_hot(torch.argmax(q_abs, dim=-1), num_classes=4) > 0.5, :]
    quat = torch.reshape(quat, batch_dim + (4,))
    return quat


def axis_angle_to_matrix(
    axis: Float[torch.Tensor, "... 3"], angle: Float[torch.Tensor, "..."]
) -> Float[torch.Tensor, "... 3 3"]:
    """
    Converts axis angles to rotation matrices using Rodrigues formula.

    Args:
        axis (torch.Tensor): axis, the shape could be [..., 3].
        angle (torch.Tensor): angle, the shape could be [...].

    Returns:
        torch.Tensor: Rotation matrices [..., 3, 3].

    Example:
        >>> axis = torch.tensor([1.0, 0.0, 0.0])
        >>> angle = torch.tensor(0.5)
        >>> axis_angle_to_matrix(axis, angle)
        tensor([[ 1.0000,  0.0000,  0.0000],
                [ 0.0000,  0.8776, -0.4794],
                [ 0.0000,  0.4794,  0.8776]])
    """
    x, y, z = torch.unbind(axis, -1)
    s, c = torch.sin(angle), torch.cos(angle)
    C = 1 - c

    xs, ys, zs = x * s, y * s, z * s
    xC, yC, zC = x * C, y * C, z * C
    xyC, yzC, zxC = x * yC, y * zC, z * xC

    # fmt: off
    rot_mat = torch.stack([x * xC + c, xyC - zs, zxC + ys,
                          xyC + zs, y * yC + c, yzC - xs,
                          zxC - ys, yzC + xs, z * zC + c], dim=-1).reshape(angle.shape + (3, 3))
    # fmt: on
    return rot_mat


def _index_from_letter(letter: str) -> int:
    if letter not in "xyz":
        raise ValueError(f"{letter} is not a valid axis letter")
    return "xyz".index(letter)


def _angle_from_tan(axis, other_axis, data, horizontal, tait_bryan):
    """
    Extract the first or third Euler angle from the two members of
    the matrix which are positive constant times its sine and cosine.

    Args:
        axis: Axis label "x" or "y or "z" for the angle we are finding.
        other_axis: Axis label "x" or "y or "z" for the middle axis in the
            convention.
        data: Rotation matrices as tensor of shape (..., 3, 3).
        horizontal: Whether we are looking for the angle for the third axis,
            which means the relevant entries are in the same row of the
            rotation matrix. If not, they are in the same column.
        tait_bryan: Whether the first and third axes in the convention differ.

    Returns:
        Euler Angles in radians for each matrix in data as a tensor
        of shape (...).
    """
    i1, i2 = {"x": (2, 1), "y": (0, 2), "z": (1, 0)}[axis]
    if horizontal:
        i2, i1 = i1, i2
    even = (axis + other_axis) in ["xy", "yz", "zx"]
    if isinstance(data, np.ndarray):
        if horizontal == even:
            return np.arctan2(data[..., i1], data[..., i2])
        if tait_bryan:
            return np.arctan2(-data[..., i2], data[..., i1])
        return np.arctan2(data[..., i2], -data[..., i1])
    elif isinstance(data, torch.Tensor):
        if horizontal == even:
            return torch.atan2(data[..., i1], data[..., i2])
        if tait_bryan:
            return torch.atan2(-data[..., i2], data[..., i1])
        return torch.atan2(data[..., i2], -data[..., i1])
    else:
        raise ValueError("data must be a numpy array or torch tensor")


def matrix_to_euler_angles(matrix: Tensor, convention: str = "xyz") -> Tensor:
    """
    Convert rotations given as rotation matrices to Euler angles in radians.

    Args:
        matrix: Rotation matrices with shape (..., 3, 3).
        convention: Convention string of 3/4 letters, e.g. "xyz", "sxyz", "rxyz", "exyz".
            If the length is 3, the extrinsic rotation is assumed.
            If the length is 4, the first character is "r/i" (rotating/intrinsic), or "s/e" (static / extrinsic).
            The remaining characters are the axis "x, y, z" in the order.

    Returns:
        Euler angles in radians with shape (..., 3).
    """
    convention = convention.lower()
    extrinsic = True
    if len(convention) != 3 and len(convention) != 4:
        raise ValueError(f"{convention} is not a valid convention")
    if len(convention) == 4:
        if convention[0] not in ["r", "i", "s", "e"]:
            raise ValueError(f"{convention[0]} is not a valid first character for a convention")
        extrinsic = convention[0] in ["s", "e"]
        convention = convention[1:]

    if not extrinsic:  # intrinsic
        convention = convention[::-1]  # reverse order

    i0 = _index_from_letter(convention[0])
    i2 = _index_from_letter(convention[2])
    tait_bryan = i0 != i2

    matrix = torch.as_tensor(matrix)
    if tait_bryan:
        central_angle = torch.asin(matrix[..., i2, i0] * (-1.0 if i2 - i0 in [-1, 2] else 1.0))
    else:
        central_angle = torch.acos(matrix[..., i2, i2])

    angle3 = _angle_from_tan(convention[2], convention[1], matrix[..., i0], False, tait_bryan)
    angle1 = _angle_from_tan(convention[0], convention[1], matrix[..., i2, :], True, tait_bryan)
    if not extrinsic:
        angle3, angle1 = angle1, angle3
    return torch.stack([angle1, central_angle, angle3], -1)  # type: ignore


def _axis_angle_rotation(axis, angle):
    """
    Return the rotation matrices for one of the rotations about an axis
    of which Euler angles describe, for each value of the angle given.

    Args:
        axis: Axis label "x" or "y or "z".
        angle: Any shape tensor of Euler angles in radians

    Returns:
        Rotation matrices as tensor of shape (..., 3, 3).
    """
    cos = torch.cos(angle)
    sin = torch.sin(angle)
    one = torch.ones_like(angle)
    zero = torch.zeros_like(angle)
    if axis == "x":
        R_flat = (one, zero, zero, zero, cos, -sin, zero, sin, cos)
    elif axis == "y":
        R_flat = (cos, zero, sin, zero, one, zero, -sin, zero, cos)
    elif axis == "z":
        R_flat = (cos, -sin, zero, sin, cos, zero, zero, zero, one)
    else:
        raise ValueError("letter must be either X, Y or Z.")
    return torch.reshape(torch.stack(R_flat, -1), angle.shape + (3, 3))


# fmt: off
_AXES = Literal[
    "sxyz", "sxyx", "sxzy", "sxzx", "syzx", "syzy", "syxz", "syxy", "szxy", "szxz", "szyx", "szyz",
    "rzyx", "rxyx", "ryzx", "rxzx", "rxzy", "ryzy", "rzxy", "ryxy", "ryxz", "rzxz", "rxyz", "rzyz"
]
# fmt: on
_VALID_AXES: Dict[_AXES, None] = {axes: None for axes in get_args(_AXES)}


def euler_angles_to_matrix(
    euler_angles: Float[torch.Tensor, "... 3"], axes: _AXES = "sxyz"
) -> Float[torch.Tensor, "... 3 3"]:
    """Converts Euler angles to rotation matrices.

    Args:
        euler_angles (torch.Tensor): Euler angles, the shape could be [..., 3].
        axes (str): Axis specification; one of 24 axis string sequences - e.g. `sxyz (the default). It's recommended to use the full name of the axes, e.g. "sxyz" instead of "xyz", but if 3 characters are provided, it will be prefixed with "s".

    Returns:
        torch.Tensor: Rotation matrices [..., 3, 3].

    Example:
        >>> euler_angles = torch.tensor([1.0, 0.5, 2.0])
        >>> euler_angles_to_matrix(euler_angles, axes="sxyz")
        tensor([[-0.3652, -0.6592,  0.6574],
                [ 0.7980,  0.1420,  0.5857],
                [-0.4794,  0.7385,  0.4742]])
        >>> euler_angles_to_matrix(euler_angles, axes="rxyz")
        tensor([[-0.3652, -0.7980,  0.4794],
                [ 0.3234, -0.5917, -0.7385],
                [ 0.8729, -0.1146,  0.4742]])
    """
    axes = axes.lower()  # type: ignore
    if len(axes) == 3:
        axes = f"s{axes}"  # type: ignore
    if axes not in _VALID_AXES:
        raise ValueError(f"Invalid axes: {axes}")

    matrices = [_axis_angle_rotation(c, e) for c, e in zip(axes[1:], torch.unbind(euler_angles, -1))]
    if axes[0] == "s":
        return torch.matmul(torch.matmul(matrices[2], matrices[1]), matrices[0])
    else:
        return torch.matmul(torch.matmul(matrices[0], matrices[1]), matrices[2])


def rotation_6d_to_matrix(d6: Tensor) -> Tensor:
    """Converts 6D rotation representation by Zhou et al. [1] to rotation matrix
    using Gram--Schmidt orthogonalization per Section B of [1].

    Args:
        d6 (Tensor): 6D rotation representation of shape [..., 6]

    Returns:
        Tensor: Rotation matrices of shape [..., 3, 3]

    [1] Zhou, Y., Barnes, C., Lu, J., Yang, J., & Li, H.
    On the Continuity of Rotation Representations in Neural Networks. CVPR 2019. arxiv_

    `pytorch3d implementation`_

    .. _arxiv: https://arxiv.org/pdf/1812.07035
    .. _`pytorch3d implementation`: https://github.com/facebookresearch/pytorch3d/blob/bd52f4a408b29dc6b4357b70c93fd7a9749ca820/pytorch3d/transforms/rotation_conversions.py#L558
    """
    a1, a2 = d6[..., :3], d6[..., 3:]
    b1 = F.normalize(a1, dim=-1)
    b2 = a2 - torch.sum(b1 * a2, dim=-1, keepdim=True) * b1
    b2 = F.normalize(b2, dim=-1)
    b3 = torch.cross(b1, b2, dim=-1)
    return torch.stack((b1, b2, b3), dim=-2)


def matrix_to_rotation_6d(matrix: Tensor) -> Tensor:
    """Converts rotation matrices to 6D rotation representation by Zhou et al. [1]
    by dropping the last row. Note that 6D representation is not unique.

    Args:
        matrix: batch of rotation matrices of size [..., 3, 3]
    Returns:
        6D rotation representation, of shape [..., 6]

    [1] Zhou, Y., Barnes, C., Lu, J., Yang, J., & Li, H.
    On the Continuity of Rotation Representations in Neural Networks. CVPR 2019. arxiv_

    .. _arxiv: https://arxiv.org/pdf/1812.07035
    """
    batch_dim = matrix.shape[:-2]
    return torch.reshape(torch.clone(matrix[..., :2, :]), batch_dim + (6,))


__all__ = [
    "axis_angle_to_matrix",
    "axis_angle_vector_to_quaternion",
    "compose_axis_angle_vector",
    "euler_angles_to_matrix",
    "matrix_to_euler_angles",
    "matrix_to_quaternion",
    "matrix_to_rotation_6d",
    "quaternion_real_to_first",
    "quaternion_real_to_last",
    "quaternion_to_axis_angle_vector",
    "quaternion_to_matrix",
    "random_rotation_matrix",
    "rotation_6d_to_matrix",
    "split_axis_angle_vector",
    "standardize_quaternion",
]
