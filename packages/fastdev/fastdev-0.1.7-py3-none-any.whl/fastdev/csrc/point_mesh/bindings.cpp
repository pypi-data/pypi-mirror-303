#include "point_mesh/point_mesh.h"
#include "utils/cuda_utils.h"
#include <torch/extension.h>

std::tuple<torch::Tensor, torch::Tensor, torch::Tensor> ClosestPointOnMesh(
    const torch::Tensor &points, const torch::Tensor &points_first_idx,
    const torch::Tensor &triangles, const torch::Tensor &triangles_first_idx,
    const int64_t max_points_per_batch, const double min_triangle_area) {
    if (points.is_cuda()) {
#ifdef WITH_CUDA
        CHECK_CUDA(points);
        CHECK_CUDA(points_first_idx);
        CHECK_CUDA(triangles);
        CHECK_CUDA(triangles_first_idx);
        return ClosestPointOnMeshCuda(points, points_first_idx, triangles,
                                      triangles_first_idx, max_points_per_batch,
                                      min_triangle_area);
#else
        AT_ERROR("Not compiled with GPU support");
#endif
    } else {
        return ClosestPointOnMeshCpu(points, points_first_idx, triangles,
                                     triangles_first_idx, min_triangle_area);
    }
}

PYBIND11_MODULE(fastdev_point_mesh, m) {
    m.def("closest_point_on_mesh", &ClosestPointOnMesh);
}
