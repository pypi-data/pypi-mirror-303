#!/usr/bin/env python3

import numpy as np
from remontee import remontee
from tests import test_gauss, run_test


def gauss(A_in, B_in):
    """
    can't pass all tests every time...
    """
    # we make a copy to avoid modifying the original matrices
    A, B = A_in.copy(), B_in.copy()
    m = np.shape(B)[0]
    g = np.matrix(np.zeros((m, m)))
    for k in range(m):
        if A[k, k] == 0:
            continue
        for i in range(k + 1, m):
            g[i, k] = A[i, k] / A[k, k]
            for j in range(k, m):
                # you can start at k + 1 but starting at k
                # adds zeros underneath the diagonal, showing
                # the matrix is indeed upper triangular
                A[i, j] = A[i, j] - g[i, k] * A[k, j]
            B[i] = B[i] - g[i, k] * B[k]
    return A, B


"""
This code FAILS for the following matrices A & B:


sage: A=matrix([[1, 2, 0, 0, 0],
....:               [2, -9, 3, 4, 0],
....:               [0, 3, -12, 4, 5],
....:               [0, 4, 4, -9, 5],
....:               [0, 0, 5, 5, -5]])
sage: A
[  1   2   0   0   0]
[  2  -9   3   4   0]
[  0   3 -12   4   5]
[  0   4   4  -9   5]
[  0   0   5   5  -5]
sage: B=column_matrix([1,4,9,16,25])
sage:
sage: B
[ 1]
[ 4]
[ 9]
[16]
[25]
sage: A.solve_right(B)
[-6509/1053]
[ 3781/1053]
[  2203/351]
[ 7858/1053]
[ 9202/1053]

"""


def main():
    run_test(test_gauss, 5_000, gauss, remontee)


if __name__ == '__main__':
    main()
