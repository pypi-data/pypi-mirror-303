import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x -1

def fprime(x):
    return 3*x**2 - 1

x = 0

epsilon = 0.000001
nb_iterations = 0
x0 = 0
x = x0

while abs(f(x)) > epsilon:
    x = x - f(x) / fprime(x)

    nb_iterations += 1

print(round(x, 4))
print(nb_iterations)
print(x0)
