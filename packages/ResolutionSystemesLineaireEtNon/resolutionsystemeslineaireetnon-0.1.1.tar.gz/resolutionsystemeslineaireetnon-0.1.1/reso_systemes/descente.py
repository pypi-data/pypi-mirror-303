#!/usr/bin/env python3
import numpy as np
import numpy.linalg as alg
from tests import test_descente, run_test


def descente(A, B):
    """
    for some reason I can't get all 1000 tests to pass
    getting some numerical instability and stuff
    """
    if alg.det(A) == 0:
        return None
    m = np.shape(B)[0]
    m_idx = m - 1
    X = np.transpose(np.matrix(np.zeros(m)))
    X[0] = B[0] / A[0, 0]
    for i in range(1, m):
        if A[m_idx, m_idx] == 0 or A[i, i] == 0:
            continue
        sum = 0
        for j in range(i):
            sum += A[i, j] * X[j]
        X[i] = (B[i] - sum) / A[i, i]
    return X


def main():
    run_test(test_descente, 5_000, descente)


if __name__ == '__main__':
    main()
