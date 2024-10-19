/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
#include "utils/geometry_v2.cuh"
#include "utils/warp_reduce.cuh"
#include <ATen/cuda/Exceptions.h>
#include <c10/cuda/CUDAGuard.h>
#include <torch/extension.h>

__global__ void ClosestPointOnMeshKernel(
    const float *__restrict__ points,                // (P * 3)
    const size_t num_points,                         // P
    const float *__restrict__ triangles,             // (T * 3 * 3)
    const size_t num_triangles,                      // T
    const int64_t *__restrict__ points_first_idx,    // (B,)
    const int64_t *__restrict__ triangles_first_idx, // (B,)
    const size_t num_batches,                        // B
    float *__restrict__ closest_points,              // (P,3)
    float *__restrict__ normals,                     // (P,3)
    float *__restrict__ distances,                   // (P,)
    const double min_triangle_area) {

    extern __shared__ char shared_buf[];
    float *min_dists = (float *)shared_buf; // float[NUM_THREADS]
    int64_t *min_idxs =
        (int64_t *)&min_dists[blockDim.x]; // int64_t[NUM_THREADS]

    const size_t batch_idx = blockIdx.y; // index of batch element.
    const size_t point_idx_in_batch = blockIdx.x;
    const size_t thread_idx = threadIdx.x;

    // start and end index of points
    const int64_t start_point_idx = points_first_idx[batch_idx];
    const int64_t end_point_idx = (batch_idx == num_batches - 1)
                                      ? num_points
                                      : points_first_idx[batch_idx + 1];

    // start and end index of triangles
    const size_t start_triangle_idx = triangles_first_idx[batch_idx];
    const size_t end_triangle_idx = (batch_idx == num_batches - 1)
                                        ? num_triangles
                                        : triangles_first_idx[batch_idx + 1];

    float3 *points_f3 = (float3 *)points;
    float3 *triangles_f3 = (float3 *)triangles;

    if (point_idx_in_batch < (end_point_idx - start_point_idx)) {
        float min_dist = FLT_MAX;
        size_t min_idx = 0;
        size_t point_idx = start_point_idx + point_idx_in_batch;

        for (size_t triangle_idx_in_batch = thread_idx;
             triangle_idx_in_batch < (end_triangle_idx - start_triangle_idx);
             triangle_idx_in_batch += blockDim.x) {
            size_t flat_tri_idx =
                (start_triangle_idx + triangle_idx_in_batch) * 3;

            float dist = PointTriangleDistance(
                points_f3[point_idx], triangles_f3[flat_tri_idx],
                triangles_f3[flat_tri_idx + 1], triangles_f3[flat_tri_idx + 2],
                min_triangle_area);

            if (dist < min_dist) {
                min_dist = dist;
                min_idx = start_triangle_idx + triangle_idx_in_batch;
            }
        }

        min_dists[thread_idx] = min_dist;
        min_idxs[thread_idx] = min_idx;
        __syncthreads();

        // Perform reduction in shared memory.
        for (int s = blockDim.x / 2; s > 32; s >>= 1) {
            if (thread_idx < s) {
                if (min_dists[thread_idx] > min_dists[thread_idx + s]) {
                    min_dists[thread_idx] = min_dists[thread_idx + s];
                    min_idxs[thread_idx] = min_idxs[thread_idx + s];
                }
            }
            __syncthreads();
        }

        // Unroll the last 6 iterations of the loop since they will happen
        // synchronized within a single warp.
        if (thread_idx < 32)
            WarpReduceMin<float>(min_dists, min_idxs, thread_idx);

        // Finally thread 0 writes the result to the output buffer.
        if (thread_idx == 0) {
            distances[point_idx] = min_dists[0];

            const int64_t flat_tri_idx = min_idxs[0] * 3;
            const float3 closest_point = ClosestPointOnTriangle(
                points_f3[point_idx], triangles_f3[flat_tri_idx],
                triangles_f3[flat_tri_idx + 1], triangles_f3[flat_tri_idx + 2],
                min_triangle_area);
            const float3 normal = UnitNormalOfTriangle(
                triangles_f3[flat_tri_idx], triangles_f3[flat_tri_idx + 1],
                triangles_f3[flat_tri_idx + 2]);

            atomicAdd(closest_points + point_idx * 3 + 0, closest_point.x);
            atomicAdd(closest_points + point_idx * 3 + 1, closest_point.y);
            atomicAdd(closest_points + point_idx * 3 + 2, closest_point.z);

            atomicAdd(normals + point_idx * 3 + 0, normal.x);
            atomicAdd(normals + point_idx * 3 + 1, normal.y);
            atomicAdd(normals + point_idx * 3 + 2, normal.z);
        }
    }
}

std::tuple<torch::Tensor, torch::Tensor, torch::Tensor> ClosestPointOnMeshCuda(
    const torch::Tensor &points, const torch::Tensor &points_first_idx,
    const torch::Tensor &triangles, const torch::Tensor &triangles_first_idx,
    const int64_t max_num_points_per_batch, const double min_triangle_area) {
    // check inputs
    torch::TensorArg points_t{points, "points", 1},
        points_first_idx_t{points_first_idx, "points_first_idx", 2},
        triangles_t{triangles, "triangles", 3},
        triangles_first_idx_t{triangles_first_idx, "triangles_first_idx", 4};
    torch::CheckedFrom c = "ClosestPointOnMeshCuda";
    torch::checkAllSameGPU(
        c, {points_t, points_first_idx_t, triangles_t, triangles_first_idx_t});
    torch::checkAllSameType(c, {points_t, triangles_t});

    // Set the device for the kernel launch based on the device of the input
    at::cuda::CUDAGuard device_guard(points.device());
    cudaStream_t stream = at::cuda::getCurrentCUDAStream();

    const int64_t num_points = points.size(0);
    const int64_t num_triangles = triangles.size(0);
    const int64_t num_batches = points_first_idx.size(0);
    TORCH_CHECK(triangles_first_idx.size(0) == num_batches,
                "points_first_idx and triangles_first_idx must have the same "
                "batch size");
    TORCH_CHECK(points.size(1) == 3, "points must be of shape (N, 3)");
    TORCH_CHECK(triangles.size(1) == 3 && triangles.size(2) == 3,
                "triangles must be of shape (N, 3, 3)");

    // clang-format off
    torch::Tensor closest_points = torch::zeros({num_points, 3}, points.options());
    torch::Tensor normals = torch::zeros({num_points, 3}, points.options());
    torch::Tensor distances = torch::zeros({num_points}, points.options());
    // clang-format on

    if (num_points == 0) {
        AT_CUDA_CHECK(cudaGetLastError());
        return std::make_tuple(closest_points, normals, distances);
    }

    const int threads = 128;
    const dim3 blocks(max_num_points_per_batch, num_batches);
    size_t shared_size = threads * sizeof(size_t) + threads * sizeof(int64_t);
    ClosestPointOnMeshKernel<<<blocks, threads, shared_size, stream>>>(
        points.contiguous().data_ptr<float>(), num_points,
        triangles.contiguous().data_ptr<float>(), num_triangles,
        points_first_idx.contiguous().data_ptr<int64_t>(),
        triangles_first_idx.contiguous().data_ptr<int64_t>(), num_batches,
        closest_points.data_ptr<float>(), normals.data_ptr<float>(),
        distances.data_ptr<float>(), min_triangle_area);

    AT_CUDA_CHECK(cudaGetLastError());
    return std::make_tuple(closest_points, normals, distances);
}
