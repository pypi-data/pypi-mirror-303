#pragma once
#include <cmath>
#include <iostream>

// A fixed-sized vector with basic arithmetic operators useful for
// representing 3D coordinates.
template <typename T> struct vec3 {
    T x, y, z;
    typedef T scalar_t;
    vec3(T x, T y, T z) : x(x), y(y), z(z) {}
};

template <typename T>
inline vec3<T> operator+(const vec3<T> &a, const vec3<T> &b) {
    return vec3<T>(a.x + b.x, a.y + b.y, a.z + b.z);
}

template <typename T>
inline vec3<T> operator-(const vec3<T> &a, const vec3<T> &b) {
    return vec3<T>(a.x - b.x, a.y - b.y, a.z - b.z);
}

template <typename T> inline vec3<T> operator/(const vec3<T> &a, const T b) {
    if (b == 0.0) {
        throw std::runtime_error("denominator in vec3 division is 0");
    }
    return vec3<T>(a.x / b, a.y / b, a.z / b);
}

template <typename T> inline vec3<T> operator*(const T a, const vec3<T> &b) {
    return vec3<T>(a * b.x, a * b.y, a * b.z);
}

template <typename T>
inline vec3<T> operator*(const vec3<T> &a, const vec3<T> &b) {
    return vec3<T>(a.x * b.x, a.y * b.y, a.z * b.z);
}

template <typename T> inline T dot(const vec3<T> &a, const vec3<T> &b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

template <typename T> inline vec3<T> cross(const vec3<T> &a, const vec3<T> &b) {
    return vec3<T>(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x);
}

template <typename T> inline T norm(const vec3<T> &a) {
    return std::sqrt(dot(a, a));
}

template <typename T>
std::ostream &operator<<(std::ostream &os, const vec3<T> &v) {
    os << "vec3(" << v.x << ", " << v.y << ", " << v.z << ")";
    return os;
}
