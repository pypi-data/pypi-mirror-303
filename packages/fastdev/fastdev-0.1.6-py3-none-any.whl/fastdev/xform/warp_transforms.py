# mypy: disable-error-code="valid-type"
from typing import Optional, Tuple

import torch
import warp as wp
from beartype import beartype
from jaxtyping import Float


@wp.kernel
def transform_points_kernel(
    points: wp.array(dtype=wp.vec3),
    tf_mat: wp.array(dtype=wp.mat44),
    n_pts: wp.int32,
    out_pt: wp.array(dtype=wp.vec3),
):
    tid = wp.tid()
    b_idx = tid / (n_pts)
    out_pt[tid] = wp.transform_point(tf_mat[b_idx], points[tid])


class TransformPoints(torch.autograd.Function):
    @staticmethod
    def forward(ctx, pts: Float[torch.Tensor, "... n 3"], tf_mat: Float[torch.Tensor, "... 4 4"]):
        n_pts = pts.shape[-2]
        pts_wp = wp.from_torch(pts.contiguous().view(-1, 3), dtype=wp.vec3, requires_grad=pts.requires_grad)
        tf_mat_wp = wp.from_torch(
            tf_mat.contiguous().view(-1, 4, 4), dtype=wp.mat44, requires_grad=tf_mat.requires_grad
        )
        # new_pts_wp = wp.zeros_like(pts_wp)  # NOTE somehow this will cause a bug in multi-processing
        new_pts_wp = wp.from_torch(
            torch.empty_like(pts).view(-1, 3), dtype=wp.vec3, requires_grad=pts.requires_grad or tf_mat.requires_grad
        )  # NOTE do not use `torch.empty_like(pts.view(-1, 3))`, pts may not be contiguous
        wp.launch(
            kernel=transform_points_kernel,
            dim=(pts_wp.shape[0],),
            inputs=[pts_wp, tf_mat_wp, n_pts],
            outputs=[new_pts_wp],
            device=pts_wp.device,
        )
        if pts.requires_grad or tf_mat.requires_grad:
            ctx.pts_wp = pts_wp
            ctx.tf_mat_wp = tf_mat_wp
            ctx.new_pts_wp = new_pts_wp
            ctx.n_pts = n_pts
        return wp.to_torch(new_pts_wp).view(pts.shape)

    @staticmethod
    def backward(  # type: ignore
        ctx, new_pts_grad: Float[torch.Tensor, "... n 3"]
    ) -> Tuple[Optional[Float[torch.Tensor, "... n 3"]], Optional[Float[torch.Tensor, "... 4 4"]]]:
        ctx.new_pts_wp.grad = wp.from_torch(new_pts_grad.contiguous().view(-1, 3), dtype=wp.vec3)
        wp.launch(
            kernel=transform_points_kernel,
            dim=(ctx.pts_wp.shape[0],),
            inputs=[ctx.pts_wp, ctx.tf_mat_wp, ctx.n_pts],
            outputs=[ctx.new_pts_wp],
            adj_inputs=[ctx.pts_wp.grad, ctx.tf_mat_wp.grad, ctx.n_pts],
            adj_outputs=[ctx.new_pts_wp.grad],
            adjoint=True,
            device=ctx.pts_wp.device,
        )
        pts_grad = wp.to_torch(ctx.pts_wp.grad).view(new_pts_grad.shape) if ctx.pts_wp.requires_grad else None
        tf_mat_grad = (
            wp.to_torch(ctx.tf_mat_wp.grad.contiguous()).view(new_pts_grad.shape[:-2] + (4, 4))
            if ctx.tf_mat_wp.requires_grad
            else None
        )
        return pts_grad, tf_mat_grad


@beartype
def transform_points(
    pts: Float[torch.Tensor, "... n 3"], tf_mat: Float[torch.Tensor, "... 4 4"]
) -> Float[torch.Tensor, "... n 3"]:
    """Apply a transformation matrix on a set of 3D points.

    Args:
        pts (torch.Tensor): 3D points, could be [... n 3]
        tf_mat (torch.Tensor): Transformation matrix, could be [... 4 4]

    Returns:
        Transformed pts in shape of [... n 3]

    Examples:
        >>> pts = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        >>> tf_mat = torch.tensor([[0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 2.0], [1.0, 0.0, 0.0, 3.0], [0.0, 0.0, 0.0, 1.0]])
        >>> transform_points(pts, tf_mat)
        tensor([[3., 5., 4.],
                [6., 8., 7.]])

    .. note::
        The dimension number of `pts` and `tf_mat` should be the same. The batch dimensions (...) are broadcasted_ (and
        thus must be broadcastable). We don't adopt the shapes [... 3] and [... 4 4] because there is no real
        broadcasted vector-matrix multiplication in pytorch. [... 3] and [... 4 4] will be converted to [... 1 3]
        and [... 4 4] and apply a broadcasted matrix-matrix multiplication.

    .. _broadcasted: https://pytorch.org/docs/stable/notes/broadcasting.html
    """
    broadcasted_shape = torch.broadcast_shapes(pts.shape[:-2], tf_mat.shape[:-2])
    return TransformPoints.apply(
        pts.expand(broadcasted_shape + pts.shape[-2:]), tf_mat.expand(broadcasted_shape + tf_mat.shape[-2:])
    )  # type: ignore


@wp.kernel
def rotate_points_kernel(
    points: wp.array(dtype=wp.vec3),
    rot_mat: wp.array(dtype=wp.mat33),
    n_pts: wp.int32,
    out_pt: wp.array(dtype=wp.vec3),
):
    tid = wp.tid()
    b_idx = tid / (n_pts)
    out_pt[tid] = wp.mul(rot_mat[b_idx], points[tid])


class RotatePoints(torch.autograd.Function):
    @staticmethod
    def forward(ctx, pts: Float[torch.Tensor, "... n 3"], tf_mat: Float[torch.Tensor, "... 3 3"]):
        n_pts = pts.shape[-2]
        pts_wp = wp.from_torch(pts.contiguous().view(-1, 3), dtype=wp.vec3, requires_grad=pts.requires_grad)
        tf_mat_wp = wp.from_torch(
            tf_mat.contiguous().view(-1, 3, 3), dtype=wp.mat33, requires_grad=tf_mat.requires_grad
        )
        new_pts_wp = wp.from_torch(
            torch.empty_like(pts).view(-1, 3), dtype=wp.vec3, requires_grad=pts.requires_grad or tf_mat.requires_grad
        )
        wp.launch(
            kernel=rotate_points_kernel,
            dim=(pts_wp.shape[0],),
            inputs=[pts_wp, tf_mat_wp, n_pts],
            outputs=[new_pts_wp],
            device=pts_wp.device,
        )
        if pts.requires_grad or tf_mat.requires_grad:
            ctx.pts_wp = pts_wp
            ctx.tf_mat_wp = tf_mat_wp
            ctx.new_pts_wp = new_pts_wp
            ctx.n_pts = n_pts
        return wp.to_torch(new_pts_wp).view(pts.shape)

    @staticmethod
    def backward(  # type: ignore
        ctx, new_pts_grad: Float[torch.Tensor, "... n 3"]
    ) -> Tuple[Optional[Float[torch.Tensor, "... n 3"]], Optional[Float[torch.Tensor, "... 3 3"]]]:
        ctx.new_pts_wp.grad = wp.from_torch(new_pts_grad.contiguous().view(-1, 3), dtype=wp.vec3)
        wp.launch(
            kernel=rotate_points_kernel,
            dim=(ctx.pts_wp.shape[0],),
            inputs=[ctx.pts_wp, ctx.tf_mat_wp, ctx.n_pts],
            outputs=[ctx.new_pts_wp],
            adj_inputs=[ctx.pts_wp.grad, ctx.tf_mat_wp.grad, ctx.n_pts],
            adj_outputs=[ctx.new_pts_wp.grad],
            adjoint=True,
            device=ctx.pts_wp.device,
        )
        pts_grad = wp.to_torch(ctx.pts_wp.grad).view(new_pts_grad.shape) if ctx.pts_wp.requires_grad else None
        tf_mat_grad = (
            wp.to_torch(ctx.tf_mat_wp.grad).view(new_pts_grad.shape[:-2] + (3, 3))
            if ctx.tf_mat_wp.requires_grad
            else None
        )
        return pts_grad, tf_mat_grad


@beartype
def rotate_points(
    pts: Float[torch.Tensor, "... n 3"], tf_mat: Float[torch.Tensor, "... 3 3"]
) -> Float[torch.Tensor, "... n 3"]:
    """Apply a rotation matrix on a set of 3D points.

    Args:
        pts (torch.Tensor): 3D points in shape [... n 3].
        rot_mat (torch.Tensor): Rotation matrix in shape [... 3 3].

    Returns:
        torch.Tensor: Rotated points in shape [... n 3].
    """
    return RotatePoints.apply(pts, tf_mat)  # type: ignore


__all__ = ["transform_points", "rotate_points"]
