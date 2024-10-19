#include "ball_query/ball_query.h"
#include "utils/cuda_utils.h"
#include <torch/extension.h>

// Implementation which is exposed
// Note: the backward pass reuses the KNearestNeighborBackward kernel
inline std::tuple<at::Tensor, at::Tensor> BallQuery(
    const at::Tensor& p1,
    const at::Tensor& p2,
    const at::Tensor& lengths1,
    const at::Tensor& lengths2,
    int K,
    float radius) {
  if (p1.is_cuda() || p2.is_cuda()) {
#ifdef WITH_CUDA
    CHECK_CUDA(p1);
    CHECK_CUDA(p2);
    return BallQueryCuda(
        p1.contiguous(),
        p2.contiguous(),
        lengths1.contiguous(),
        lengths2.contiguous(),
        K,
        radius);
#else
    AT_ERROR("Not compiled with GPU support.");
#endif
  }
  return BallQueryCpu(
      p1.contiguous(),
      p2.contiguous(),
      lengths1.contiguous(),
      lengths2.contiguous(),
      K,
      radius);
}


PYBIND11_MODULE(fastdev_ball_query, m) {
  m.def("ball_query", &BallQuery);
}
