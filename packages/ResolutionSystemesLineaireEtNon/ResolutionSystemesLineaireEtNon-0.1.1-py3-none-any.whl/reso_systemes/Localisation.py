import numpy as np
#import math as m

station1 = np.array([2.8, 10.2, 5.2])
station2 = np.array([14, 13, 7])
station3 = np.array([4, 15, 3.5])

A = np.array([[-2*station1[0], -2*station1[1], 1],
              [-2*station2[0], -2*station2[1], 1],
              [-2*station3[0], -2*station3[1], 1]])

#B = np.array([station1[2] - m.pow(station1[0], 2) - m.pow(station1[1], 2),
#              station2[2] - m.pow(station2[0], 2) - m.pow(station2[1], 2),
#              station3[2] - m.pow(station3[0], 2) - m.pow(station3[1], 2)])

n = len(A)
X = np.zeros(n)

for k in range(n):

    if A[k][k] == 0:
        for i in range(k+1, n):
            if A[i][k] != 0:
                A[k], A[i] = A[i], A[k]
 #               B[k], B[i] = B[i], B[k]
                break
                
    for i in range(k+1, n):
        g = A[i][k] / A[k][k]
        for j in range(k+1, n):
            A[i][j] = A[i][j] - g * A[k][j]
#        B[i] = B[i] - g * B[k]
        A[i][k] = 0

#X[n-1] = B[n-1] / A[n-1][n-1]

for i in range(n-2, -1, -1):
    somme = 0
    for j in range(i+1, n):
        somme += A[i][j] * X[j]
#    X[i] = (B[i] - somme) / A[i][i]

print("Position telephone : \n", X)
