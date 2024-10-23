/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
#include "utils/geometry_v2.h"
#include "utils/vec3.h"
#include <torch/extension.h>

template <typename T>
vec3<T> ExtractPoint(const torch::TensorAccessor<T, 1> &t) {
    return vec3<T>(t[0], t[1], t[2]);
}

template <typename T>
void SetPoint(torch::TensorAccessor<T, 1> &&t, const vec3<T> &point) {
    t[0] = point.x;
    t[1] = point.y;
    t[2] = point.z;
}

std::tuple<torch::Tensor, torch::Tensor, torch::Tensor> ClosestPointOnMeshCpu(
    const torch::Tensor &points, const torch::Tensor &points_first_idx,
    const torch::Tensor &triangles, const torch::Tensor &triangles_first_idx,
    const double min_triangle_area) {
    const int64_t num_points = points.size(0);
    const int64_t num_triangles = triangles.size(0);
    const int64_t num_batches = points_first_idx.size(0);

    TORCH_CHECK(points.size(1) == 3, "points must have shape (P, 3)");
    TORCH_CHECK(triangles.size(1) == 3 && triangles.size(2) == 3,
                "triangles must have shape (T, 3, 3)");
    TORCH_CHECK(triangles_first_idx.size(0) == num_batches,
                "Triangles batch size must match points batch size");

    // clang-format off
    torch::Tensor closest_points = torch::zeros({num_points, 3}, points.options());
    torch::Tensor normals = torch::zeros({num_points, 3}, points.options());
    torch::Tensor distances = torch::zeros({num_points}, points.options());
    // clang-format on

    auto points_a = points.accessor<float, 2>();
    auto points_first_idx_a = points_first_idx.accessor<int64_t, 1>();
    auto triangles_a = triangles.accessor<float, 3>();
    auto triangles_first_idx_a = triangles_first_idx.accessor<int64_t, 1>();
    auto closest_points_a = closest_points.accessor<float, 2>();
    auto normals_a = normals.accessor<float, 2>();
    auto distances_a = distances.accessor<float, 1>();

    int64_t batch_idx = 0;
    int64_t points_batch_end = 0;
    int64_t triangles_batch_start = 0, triangles_batch_end = 0;

    for (int64_t point_idx = 0; point_idx < num_points; point_idx++) {
        if (point_idx == points_batch_end) {
            batch_idx++;
            triangles_batch_start = triangles_batch_end;

            if (batch_idx == num_batches) {
                points_batch_end = num_points;
                triangles_batch_end = num_triangles;
            } else {
                points_batch_end = points_first_idx_a[batch_idx];
                triangles_batch_end = triangles_first_idx_a[batch_idx];
            }
        }

        float min_distance = std::numeric_limits<float>::max();
        int64_t min_triangle_idx = 0;

        vec3<float> point = ExtractPoint(points_a[point_idx]);

        for (int64_t triangle_idx = triangles_batch_start;
             triangle_idx < triangles_batch_end; triangle_idx++) {
            float distance = PointTriangleDistance(
                point, ExtractPoint(triangles_a[triangle_idx][0]),
                ExtractPoint(triangles_a[triangle_idx][1]),
                ExtractPoint(triangles_a[triangle_idx][2]), min_triangle_area);

            if (distance < min_distance) {
                min_distance = distance;
                min_triangle_idx = triangle_idx;
            }
        }
        distances_a[point_idx] = min_distance;

        vec3<float> closest_point = ClosestPointOnTriangle(
            point, ExtractPoint(triangles_a[min_triangle_idx][0]),
            ExtractPoint(triangles_a[min_triangle_idx][1]),
            ExtractPoint(triangles_a[min_triangle_idx][2]), min_triangle_area);
        SetPoint(closest_points_a[point_idx], closest_point);

        vec3<float> normal = UnitNormalOfTriangle(
            ExtractPoint(triangles_a[min_triangle_idx][0]),
            ExtractPoint(triangles_a[min_triangle_idx][1]),
            ExtractPoint(triangles_a[min_triangle_idx][2]));
        SetPoint(normals_a[point_idx], normal);
    }

    return std::make_tuple(closest_points, normals, distances);
}
