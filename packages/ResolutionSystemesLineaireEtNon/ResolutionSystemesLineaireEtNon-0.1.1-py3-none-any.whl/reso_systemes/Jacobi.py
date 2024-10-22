import numpy as np

A = np.array([[-6, 1, -1, 0],
              [1, 4, 0, 1],
              [-1, 0, -6, 2],
              [0, 1, 2, 6]])
              
n = len(A)

B = np.array([-3, 9, -2, 0])

X = np.zeros(n)

D = np.zeros((n, n))
L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(len(A)):
    for j in range(len(A)):
        if i == j:
            D[i][j] = A[i][j]
        elif i > j:
            L[i][j] = -A[i][j]
        elif j > i:
            U[i][j] = -A[i][j]

epsilon = 0.001
r = B - np.dot(A, X)
ca = np.linalg.norm(r) / np.linalg.norm(B)

X_new = X

# Jacobi
while ca > epsilon:
    X_new = np.dot(np.linalg.inv(D), np.dot(L + U, X)) + np.dot(np.linalg.inv(D), B)
    
    r = B - np.dot(A, X)
    ca = np.linalg.norm(r) / np.linalg.norm(B)

    X = X_new

print("Jacobi", X_new)
