/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
#pragma once
#include <thrust/tuple.h>

const auto vEpsilon = 1e-8;

__device__ inline float FloatMin3(const float a, const float b, const float c) {
    return fminf(a, fminf(b, c));
}

__device__ inline float FloatMax3(const float a, const float b, const float c) {
    return fmaxf(a, fmaxf(b, c));
}

// Common functions and operators for float3.
__device__ inline float3 operator-(const float3 &a, const float3 &b) {
    return make_float3(a.x - b.x, a.y - b.y, a.z - b.z);
}

__device__ inline float3 operator+(const float3 &a, const float3 &b) {
    return make_float3(a.x + b.x, a.y + b.y, a.z + b.z);
}

__device__ inline float3 operator/(const float3 &a, const float3 &b) {
    return make_float3(a.x / b.x, a.y / b.y, a.z / b.z);
}

__device__ inline float3 operator/(const float3 &a, const float b) {
    return make_float3(a.x / b, a.y / b, a.z / b);
}

__device__ inline float3 operator*(const float3 &a, const float3 &b) {
    return make_float3(a.x * b.x, a.y * b.y, a.z * b.z);
}

__device__ inline float3 operator*(const float a, const float3 &b) {
    return make_float3(a * b.x, a * b.y, a * b.z);
}

__device__ inline float dot(const float3 &a, const float3 &b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

__device__ inline float sum(const float3 &a) { return a.x + a.y + a.z; }

__device__ inline float3 cross(const float3 &a, const float3 &b) {
    return make_float3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z,
                       a.x * b.y - a.y * b.x);
}
__device__ inline float norm(const float3 &a) { return sqrt(dot(a, a)); }

__device__ inline float3 normalize(const float3 &a) {
    return a / (norm(a) + vEpsilon);
}
