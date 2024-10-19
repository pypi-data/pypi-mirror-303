#pragma once

#include "utils/float_math.cuh"

const double kEpsilon = 1e-8;
const double vEpislon = 1e-8;

__device__ inline float AreaOfTriangle(const float3 &v0, const float3 &v1,
                                       const float3 &v2) {
    float3 p0 = v1 - v0;
    float3 p1 = v2 - v0;

    // compute the hypotenus of the scross product (p0 x p1)
    float dd =
        hypot(p0.y * p1.z - p0.z * p1.y,
              hypot(p0.z * p1.x - p0.x * p1.z, p0.x * p1.y - p0.y * p1.x));

    return dd / 2.0;
}

__device__ inline float3 BarycentricCoords(const float3 &p, const float3 &v0,
                                           const float3 &v1, const float3 &v2) {
    float3 p0 = v1 - v0;
    float3 p1 = v2 - v0;
    float3 p2 = p - v0;

    const float d00 = dot(p0, p0);
    const float d01 = dot(p0, p1);
    const float d11 = dot(p1, p1);
    const float d20 = dot(p2, p0);
    const float d21 = dot(p2, p1);

    const float denom = d00 * d11 - d01 * d01 + kEpsilon;
    const float w1 = (d11 * d20 - d01 * d21) / denom;
    const float w2 = (d00 * d21 - d01 * d20) / denom;
    const float w0 = 1.0f - w1 - w2;

    return make_float3(w0, w1, w2);
}

__device__ inline bool IsInsideTriangle(const float3 &p, const float3 &v0,
                                        const float3 &v1, const float3 &v2,
                                        const double min_triangle_area) {
    bool inside;
    if (AreaOfTriangle(v0, v1, v2) < min_triangle_area) {
        inside = 0;
    } else {
        float3 bary = BarycentricCoords(p, v0, v1, v2);
        bool x_in = 0.0f <= bary.x && bary.x <= 1.0f;
        bool y_in = 0.0f <= bary.y && bary.y <= 1.0f;
        bool z_in = 0.0f <= bary.z && bary.z <= 1.0f;
        inside = x_in && y_in && z_in;
    }
    return inside;
}

__device__ inline float PointLineDistance(const float3 &p, const float3 &v0,
                                          const float3 &v1) {
    const float3 v1v0 = v1 - v0;
    const float3 pv0 = p - v0;
    const float t_bot = dot(v1v0, v1v0);
    const float t_top = dot(pv0, v1v0);
    // if t_bot small, then v0 == v1, set tt to 0.
    float tt = (t_bot < kEpsilon) ? 0.0f : (t_top / t_bot);

    tt = __saturatef(tt); // clamps to [0, 1]

    const float3 p_proj = v0 + tt * v1v0;
    const float3 diff = p - p_proj;
    const float dist = dot(diff, diff);
    return dist;
}

__device__ inline float PointTriangleDistance(const float3 &p, const float3 &v0,
                                              const float3 &v1,
                                              const float3 &v2,
                                              const double min_triangle_area) {
    float3 normal = cross(v2 - v0, v1 - v0);
    const float norm_normal = norm(normal);
    normal = normalize(normal);

    // p0 is the projection of p on the plane spanned by (v0, v1, v2)
    // i.e. p0 = p + t * normal, s.t. (p0 - v0) is orthogonal to normal
    const float t = dot(v0 - p, normal);
    const float3 p0 = p + t * normal;

    bool is_inside = IsInsideTriangle(p0, v0, v1, v2, min_triangle_area);
    float dist = 0.0f;

    if ((is_inside) && (norm_normal > kEpsilon)) {
        // if projection p0 is inside triangle spanned by (v0, v1, v2)
        // then distance is equal to norm(p0 - p)^2
        dist = t * t;
    } else {
        const float e01 = PointLineDistance(p, v0, v1);
        const float e02 = PointLineDistance(p, v0, v2);
        const float e12 = PointLineDistance(p, v1, v2);

        dist = (e01 > e02) ? e02 : e01;
        dist = (dist > e12) ? e12 : dist;
    }

    return dist;
}

__device__ inline float3
UnitNormalOfTriangle(const float3 &v0, const float3 &v1, const float3 &v2) {
    float3 normal = cross(v1 - v0, v2 - v0);
    const float norm_normal = norm(normal);
    normal = normalize(normal);
    return normal;
}

__device__ inline float3 ClosestPointOnLine(const float3 &p, const float3 &v0,
                                            const float3 &v1) {
    const float3 v1v0 = v1 - v0;
    const float3 pv0 = p - v0;
    const float t_bot = dot(v1v0, v1v0);
    const float t_top = dot(pv0, v1v0);
    // if t_bot small, then v0 == v1, set tt to 0.
    float tt = (t_bot < kEpsilon) ? 0.0f : (t_top / t_bot);

    tt = __saturatef(tt); // clamps to [0, 1]

    const float3 p_proj = v0 + tt * v1v0;
    return p_proj;
}

__device__ inline float3
ClosestPointOnTriangle(const float3 &p, const float3 &v0, const float3 &v1,
                       const float3 &v2, const double min_triangle_area) {
    float3 normal = cross(v2 - v0, v1 - v0);
    const float norm_normal = norm(normal);
    normal = normalize(normal);

    // p0 is the projection of p on the plane spanned by (v0, v1, v2)
    // i.e. p0 = p + t * normal, s.t. (p0 - v0) is orthogonal to normal
    const float t = dot(v0 - p, normal);
    const float3 p0 = p + t * normal;

    bool is_inside = IsInsideTriangle(p0, v0, v1, v2, min_triangle_area);

    if ((is_inside) && (norm_normal > kEpsilon)) {
        return p0;
    } else {
        const float e01 = PointLineDistance(p, v0, v1);
        const float e02 = PointLineDistance(p, v0, v2);
        const float e12 = PointLineDistance(p, v1, v2);

        if (e01 < e02 && e01 < e12) {
            return ClosestPointOnLine(p, v0, v1);
        } else if (e02 < e01 && e02 < e12) {
            return ClosestPointOnLine(p, v0, v2);
        } else {
            return ClosestPointOnLine(p, v1, v2);
        }
    }
}
