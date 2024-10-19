/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
#pragma once

#include "utils/vec3.h"

const double kEpsilon = 1e-8;
const double vEpislon = 1e-8;

// Computes the area of a triangle (v0, v1, v2).
// Args:
//     v0, v1, v2: vec3 coordinates of the triangle vertices
//
// Returns:
//     area: float: the area of the triangle
//
template <typename T>
T AreaOfTriangle(const vec3<T> &v0, const vec3<T> &v1, const vec3<T> &v2) {
    vec3<T> p0 = v1 - v0;
    vec3<T> p1 = v2 - v0;

    // compute the hypotenus of the scross product (p0 x p1)
    T dd = std::hypot(
        p0.y * p1.z - p0.z * p1.y,
        std::hypot(p0.z * p1.x - p0.x * p1.z, p0.x * p1.y - p0.y * p1.x));

    return dd / 2.0;
}

template <typename T>
vec3<T> BarycentricCoords(const vec3<T> &p, const vec3<T> &v0,
                          const vec3<T> &v1, const vec3<T> &v2) {
    vec3<T> p0 = v1 - v0;
    vec3<T> p1 = v2 - v0;
    vec3<T> p2 = p - v0;

    const T d00 = dot(p0, p0);
    const T d01 = dot(p0, p1);
    const T d11 = dot(p1, p1);
    const T d20 = dot(p2, p0);
    const T d21 = dot(p2, p1);

    const T denom = d00 * d11 - d01 * d01 + static_cast<T>(kEpsilon);
    const T w1 = (d11 * d20 - d01 * d21) / denom;
    const T w2 = (d00 * d21 - d01 * d20) / denom;
    const T w0 = 1.0f - w1 - w2;

    return vec3<T>(w0, w1, w2);
}

// Checks whether the point p is inside the triangle (v0, v1, v2).
// A point is inside the triangle, if all barycentric coordinates
// wrt the triangle are >= 0 & <= 1.
// If the triangle is degenerate, aka line or point, then return False.
//
// NOTE that this function assumes that p lives on the space spanned
// by (v0, v1, v2).
//
// Args:
//     p: vec3 coordinates of a point
//     v0, v1, v2: vec3 coordinates of the triangle vertices
//     min_triangle_area: triangles less than this size are considered
//     points/lines, IsInsideTriangle returns False
//
// Returns:
//     inside: bool indicating wether p is inside triangle
//
template <typename T>
static bool IsInsideTriangle(const vec3<T> &p, const vec3<T> &v0,
                             const vec3<T> &v1, const vec3<T> &v2,
                             const double min_triangle_area) {
    bool inside;
    if (AreaOfTriangle(v0, v1, v2) < min_triangle_area) {
        inside = 0;
    } else {
        vec3<T> bary = BarycentricCoords(p, v0, v1, v2);
        bool x_in = 0.0f <= bary.x && bary.x <= 1.0f;
        bool y_in = 0.0f <= bary.y && bary.y <= 1.0f;
        bool z_in = 0.0f <= bary.z && bary.z <= 1.0f;
        inside = x_in && y_in && z_in;
    }
    return inside;
}

template <typename T>
T PointLineDistance(const vec3<T> &p, const vec3<T> &v0, const vec3<T> &v1) {
    const vec3<T> v1v0 = v1 - v0;
    const T l2 = dot(v1v0, v1v0);
    if (l2 <= static_cast<T>(kEpsilon)) {
        return dot(p - v1, p - v1);
    }

    const T t = dot(v1v0, p - v0) / l2;
    const T tt =
        std::min(std::max(t, static_cast<T>(0.0)), static_cast<T>(1.0));
    const vec3<T> p_proj = v0 + tt * v1v0;
    return dot(p - p_proj, p - p_proj);
}

template <typename T>
T PointTriangleDistance(const vec3<T> &p, const vec3<T> &v0, const vec3<T> &v1,
                        const vec3<T> &v2, const double min_triangle_area) {
    // compute the normal of the triangle
    vec3<T> normal = cross(v1 - v0, v2 - v0);
    const T normal_norm = norm(normal);
    normal = normal / (normal_norm + static_cast<T>(vEpislon)); // normalize

    // p0 is the projection of p on the plane spanned by (v0, v1, v2)
    // i.e. p0 = p + t * normal, s.t. (p0 - v0) is orthogonal to normal
    const T t = dot(v0 - p, normal);
    const vec3<T> p0 = p + t * normal;

    bool is_inside = IsInsideTriangle(p0, v0, v1, v2, min_triangle_area);
    T dist = 0.0f;

    if ((is_inside) && (normal_norm > static_cast<T>(kEpsilon))) {
        // if projection p0 is inside triangle spanned by (v0, v1, v2)
        // then distance is equal to norm(p0 - p)^2
        dist = t * t;
    } else {
        const T e01 = PointLineDistance(p, v0, v1);
        const T e02 = PointLineDistance(p, v0, v2);
        const T e12 = PointLineDistance(p, v1, v2);

        dist = (e01 > e02) ? e02 : e01;
        dist = (dist > e12) ? e12 : dist;
    }

    return dist;
}

template <typename T>
vec3<T> UnitNormalOfTriangle(const vec3<T> &v0, const vec3<T> &v1,
                             const vec3<T> &v2) {
    vec3<T> normal = cross(v1 - v0, v2 - v0);
    const T normal_norm = norm(normal);
    normal = normal / (normal_norm + static_cast<T>(vEpislon)); // normalize
    return normal;
}

template <typename T>
vec3<T> ClosestPointOnLine(const vec3<T> &p, const vec3<T> &v0,
                           const vec3<T> &v1) {
    const vec3<T> v1v0 = v1 - v0;
    const T l2 = dot(v1v0, v1v0);
    if (l2 <= static_cast<T>(kEpsilon)) {
        return v1;
    }

    const T t = dot(v1v0, p - v0) / l2;
    const T tt =
        std::min(std::max(t, static_cast<T>(0.0)), static_cast<T>(1.0));
    const vec3<T> p_proj = v0 + tt * v1v0;
    return p_proj;
}

template <typename T>
vec3<T> ClosestPointOnTriangle(const vec3<T> &p, const vec3<T> &v0,
                               const vec3<T> &v1, const vec3<T> &v2,
                               const double min_triangle_area) {
    // compute the normal of the triangle
    vec3<T> normal = cross(v1 - v0, v2 - v0);
    const T normal_norm = norm(normal);
    normal = normal / (normal_norm + static_cast<T>(vEpislon)); // normalize

    // p0 is the projection of p on the plane spanned by (v0, v1, v2)
    // i.e. p0 = p + t * normal, s.t. (p0 - v0) is orthogonal to normal
    const T t = dot(v0 - p, normal);
    const vec3<T> p0 = p + t * normal;

    bool is_inside = IsInsideTriangle(p0, v0, v1, v2, min_triangle_area);
    if ((is_inside) && (normal_norm > static_cast<T>(kEpsilon))) {
        return p0;
    } else {
        const T e01 = PointLineDistance(p, v0, v1);
        const T e02 = PointLineDistance(p, v0, v2);
        const T e12 = PointLineDistance(p, v1, v2);

        if (e01 <= e02 && e01 <= e12) {
            return ClosestPointOnLine(p, v0, v1);
        } else if (e02 <= e01 && e02 <= e12) {
            return ClosestPointOnLine(p, v0, v2);
        } else {
            return ClosestPointOnLine(p, v1, v2);
        }
    }
}
