#!/usr/bin/env python3

import numpy as np
from remontee import remontee
from descente import descente
from tests import test_cholesky, run_test


def cholesky(A):
    m = np.shape(A)[0]
    L = np.matrix(np.zeros((m, m)))
    #
    # first column
    #
    L[0, 0] = np.sqrt(A[0, 0])
    for i in range(1, m):
        L[i, 0] = A[i, 0] / L[0, 0]
    for k in range(1, m):
        #
        # l_kk coefficients (p.14)
        #
        sum_0 = 0
        for j in range(k):
            sum_0 += np.pow(L[k, j], 2)
        L[k, k] = np.sqrt(A[k, k] - sum_0)
        #
        # l_ik coefficients
        #
        for i in range(k, m):
            sum_1 = 0
            for j in range(k):
                sum_1 += L[i, j] * L[k, j]
            L[i, k] = (A[i, k] - sum_1) / L[k, k]
    return L


def cholesky_solve(L, B):
    # two systems to solve:
    # LY = B
    # L^T X = Y
    Y = descente(L, B)
    X = remontee(np.transpose(L), Y)
    return X


def main():
    run_test(test_cholesky, 200, cholesky, cholesky_solve)


if __name__ == '__main__':
    main()
