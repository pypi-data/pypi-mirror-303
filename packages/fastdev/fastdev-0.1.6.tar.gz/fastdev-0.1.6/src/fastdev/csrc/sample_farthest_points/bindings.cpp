#include "sample_farthest_points/sample_farthest_points.h"
#include "utils/cuda_utils.h"
#include <torch/extension.h>

// Exposed implementation.
at::Tensor FarthestPointSampling(const at::Tensor &points,
                                 const at::Tensor &lengths, const at::Tensor &K,
                                 const at::Tensor &start_idxs) {
    if (points.is_cuda() || lengths.is_cuda() || K.is_cuda()) {
#ifdef WITH_CUDA
        CHECK_CUDA(points);
        CHECK_CUDA(lengths);
        CHECK_CUDA(K);
        CHECK_CUDA(start_idxs);
        return FarthestPointSamplingCuda(points, lengths, K, start_idxs);
#else
        AT_ERROR("Not compiled with GPU support.");
#endif
    }
    return FarthestPointSamplingCpu(points, lengths, K, start_idxs);
}

PYBIND11_MODULE(fastdev_sample_farthest_points, m) {
    m.def("sample_farthest_points", &FarthestPointSampling);
}
