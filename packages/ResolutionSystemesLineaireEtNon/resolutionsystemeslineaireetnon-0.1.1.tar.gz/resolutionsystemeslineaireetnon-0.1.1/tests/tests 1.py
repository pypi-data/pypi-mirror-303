import numpy as np
import numpy.linalg as alg
from random import randint
from enum import Enum


MatrixType = Enum('MatrixType', [
    'RANDOM',
    'LOWER_TRIANGULAR',
    'UPPER_TRIANGULAR',
    'SYMMETRIC_POSITIVE_DEFINITE'
])


def generate_matrix(matrix_type: MatrixType, n=-1):
    if n == -1:
        n = randint(2, 12)  # default random size
    A = np.matrix(np.zeros((n, n)))
    B = np.transpose(np.matrix(np.zeros(n)))
    must_retry = False
    while alg.det(A) == 0 or must_retry:
        if matrix_type == MatrixType.SYMMETRIC_POSITIVE_DEFINITE:
            for i in range(n):
                for j in range(i, n):
                    A[i, j] = randint(0, 99) / 10
                    A[j, i] = A[i, j]
                B[i] = randint(-99, 99) / 10
            try:
                alg.cholesky(A)
                must_retry = False
            except alg.LinAlgError:
                must_retry = True
                continue
        else:
            for i in range(n):
                range_j = range(n)
                if matrix_type == MatrixType.LOWER_TRIANGULAR:
                    range_j = range(i + 1)
                elif matrix_type == MatrixType.UPPER_TRIANGULAR:
                    range_j = range(i, n)
                for j in range_j:
                    A[i, j] = randint(-99, 99) / 10
                B[i] = randint(-99, 99) / 10
    return A, B


def display_fail(A, B, got, expected):
    print("FAILED TEST")
    print("A:")
    print(A)
    print("B:")
    print(B)
    print("got: \n", got)
    print("expected:\n", expected)


def test_remontee(remontee, show_failed=False):
    A, B = generate_matrix(MatrixType.UPPER_TRIANGULAR)
    result = remontee(A, B)
    expected = alg.solve(A, B)
    passed = np.allclose(result, expected)
    if not passed and show_failed:
        display_fail(A, B, result, expected)
    return passed


def test_descente(descente, show_failed=False):
    A, B = generate_matrix(MatrixType.LOWER_TRIANGULAR)
    result = descente(A, B)
    expected = alg.solve(A, B)
    passed = np.all(np.abs(result - expected) < 10**-6)
    if not passed and show_failed:
        display_fail(A, B, result, expected)
    return passed


def test_gauss(gaussian_elim, remontee, show_failed=False):
    A, B = generate_matrix(MatrixType.RANDOM)
    trig_A, trig_B = gaussian_elim(A, B)
    result = remontee(trig_A, trig_B)
    expected = alg.solve(A, B)
    passed = False
    try:
        passed = np.all(np.abs(result - expected) < 10**-6)
    except Exception as e:
        print(e)
    if not passed and show_failed:
        display_fail(A, B, result, expected)
    return passed


def test_cholesky(cholesky, cholesky_solve, show_failed=False):
    A, B = generate_matrix(MatrixType.SYMMETRIC_POSITIVE_DEFINITE, randint(2, 5))
    cholesky_decomp = cholesky(A)
    expected_decomp = alg.cholesky(A)
    passed = np.allclose(cholesky_decomp, expected_decomp)
    if not passed and show_failed:
        print("CHOLESKY DECOMPOSITION FAIL")
        display_fail(A, B, cholesky_decomp, expected_decomp)
    result_solve = cholesky_solve(cholesky_decomp, B)
    expected_solve = alg.solve(A, B)
    passed_solve = np.allclose(result_solve, expected_solve)
    if not passed_solve and show_failed:
        print("CHOLESKY SOLVE FAIL")
        display_fail(A, B, result_solve, expected_solve)
    return passed and passed_solve


def run_test(test_function, num_tests, *args):
    tests_passed = 0
    for i in range(num_tests):
        if i % (num_tests // 5) == 0 and i != 0:
            print(f"Running test {i}...")
            success_rate = tests_passed / i * 100
            print(f"> Passed so far: {tests_passed}/{i} (success rate: {success_rate:.2f}%)\n")
        tests_passed += test_function(*args)
    success_rate_tot = tests_passed / num_tests * 100
    print(f"\n\n\nTests passed: {tests_passed}/{num_tests} (success rate: {success_rate_tot:.2f}%)")
