#!/usr/bin/env python3
import numpy as np
import numpy.linalg as alg
from tests import test_remontee, run_test


def remontee(A, B):
    """
    passes all tests every time
    """
    if alg.det(A) == 0:
        return None
    m = np.shape(B)[0]
    m_idx = m - 1
    X = np.transpose(np.matrix(np.zeros(m)))
    X[m_idx] = B[m_idx] / A[m_idx, m_idx]
    for i in range(m_idx - 1, -1, -1):  # iterate from m_idx to 0 inclusive
        if A[m_idx, m_idx] == 0 or A[i, i] == 0:
            continue
        sum = 0
        for j in range(i + 1, m_idx + 1):   # sums are inclusive in math!!!
            # watch out for that + 1
            sum += A[i, j] * X[j]
        X[i] = (B[i] - sum) / A[i, i]
    return X


def main():
    run_test(test_remontee, 5000, remontee)


if __name__ == '__main__':
    main()
