#pragma once
#include <torch/extension.h>

// ****************************************************************************
// *                        ClosestPointOnMesh                                *
// ****************************************************************************

// Computs the closest point on mesh surface for each p in points.
//
// Args:
//     points: FloatTensor of shape (P, 3) of points.
//     points_first_idx: LongTensor of shape (N,) indicating the first index of
//         each instance in points.
//     triangles: FloatTensor of shape (T, 3, 3) of triangles.
//     triangles_first_idx: LongTensor of shape (N,) indicating the first index
//          of each instance in triangles.
//     min_triangle_area: triangle with area smaller than this size are
//          considered as points/lines.
//
// Returns:
//     closest_points: FloatTensor of shape (P, 3) of closest points on mesh.
//     normals: FloatTensor of shape (P, 3) of normals at closest points.
//     distances: FloatTensor of shape (P,) of distances between point and its
//         closest point on mesh.
std::tuple<torch::Tensor, torch::Tensor, torch::Tensor> ClosestPointOnMeshCpu(
    const torch::Tensor &points, const torch::Tensor &points_first_idx,
    const torch::Tensor &triangles, const torch::Tensor &triangles_first_idx,
    const double min_triangle_area);

#ifdef WITH_CUDA
std::tuple<torch::Tensor, torch::Tensor, torch::Tensor> ClosestPointOnMeshCuda(
    const torch::Tensor &points, const torch::Tensor &points_first_idx,
    const torch::Tensor &triangles, const torch::Tensor &triangles_first_idx,
    const int64_t max_points_per_batch, const double min_triangle_area);
#endif

std::tuple<torch::Tensor, torch::Tensor, torch::Tensor> ClosestPointOnMesh(
    const torch::Tensor &points, const torch::Tensor &points_first_idx,
    const torch::Tensor &triangles, const torch::Tensor &triangles_first_idx,
    const int64_t max_points_per_batch, const double min_triangle_area);
