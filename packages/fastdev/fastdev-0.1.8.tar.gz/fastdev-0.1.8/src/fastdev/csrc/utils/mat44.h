#pragma once
#include <cmath>
#include <iostream>

template <typename T> struct mat44 {
    T m[4][4];

    mat44() {
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                m[i][j] = (i == j) ? 1 : 0;
    }

    mat44(int v) {
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                m[i][j] = v;
    }

    mat44(T values[4][4]) {
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                m[i][j] = values[i][j];
    }

    mat44(T m00, T m01, T m02, T m03, T m10, T m11, T m12, T m13, T m20, T m21,
          T m22, T m23, T m30, T m31, T m32, T m33) {
        m[0][0] = m00;
        m[0][1] = m01;
        m[0][2] = m02;
        m[0][3] = m03;
        m[1][0] = m10;
        m[1][1] = m11;
        m[1][2] = m12;
        m[1][3] = m13;
        m[2][0] = m20;
        m[2][1] = m21;
        m[2][2] = m22;
        m[2][3] = m23;
        m[3][0] = m30;
        m[3][1] = m31;
        m[3][2] = m32;
        m[3][3] = m33;
    }

    mat44(T m00, T m01, T m02, T m03, T m10, T m11, T m12, T m13, T m20, T m21,
          T m22, T m23) {
        m[0][0] = m00;
        m[0][1] = m01;
        m[0][2] = m02;
        m[0][3] = m03;
        m[1][0] = m10;
        m[1][1] = m11;
        m[1][2] = m12;
        m[1][3] = m13;
        m[2][0] = m20;
        m[2][1] = m21;
        m[2][2] = m22;
        m[2][3] = m23;
        m[3][0] = 0;
        m[3][1] = 0;
        m[3][2] = 0;
        m[3][3] = 1;
    }
};

template <typename T>
inline mat44<T> operator*(const mat44<T> &a, const mat44<T> &b) {
    mat44<T> result;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            result.m[i][j] = a.m[i][0] * b.m[0][j] + a.m[i][1] * b.m[1][j] +
                             a.m[i][2] * b.m[2][j] + a.m[i][3] * b.m[3][j];
    return result;
}

template <typename T>
inline mat44<T> operator+(const mat44<T> &a, const mat44<T> &b) {
    mat44<T> result;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            result.m[i][j] = a.m[i][j] + b.m[i][j];
    return result;
}

template <typename T>
std::ostream &operator<<(std::ostream &os, const mat44<T> &m) {
    os << "mat44(";
    for (int i = 0; i < 4; ++i) {
        os << "[";
        for (int j = 0; j < 4; ++j) {
            os << m.m[i][j];
            if (j < 3)
                os << ", ";
        }
        os << "]";
        if (i < 3)
            os << ", ";
    }
    os << ")";
    return os;
}
