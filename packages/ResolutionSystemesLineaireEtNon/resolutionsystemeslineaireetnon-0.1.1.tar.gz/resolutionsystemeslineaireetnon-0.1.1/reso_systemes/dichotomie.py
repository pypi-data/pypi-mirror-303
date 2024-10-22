import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,1000)

def f(x):
    return x**3 - x -1

a, b = 1, 2
epsilon = 0.0001

x_mid = 0

while b - a >= epsilon:
    x_mid = (b + a)/2

    if f(a)*f(x_mid) < 0:
        b = x_mid
    else:
        a = x_mid

print("Solution = ", x_mid)