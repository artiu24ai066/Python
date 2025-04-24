import numpy as np
import matplotlib.pyplot as plt
import random

def get_polynomial():
    coeffs = input("Enter polynomial coefficients (highest degree first, space-separated):\n")
    coeffs = list(map(float, coeffs.strip().split()))
    return np.poly1d(coeffs)

def find_initial_interval(f, lower=-10, upper=10):
    while True:
        a = random.uniform(lower, upper)
        b = random.uniform(lower, upper)
        if a > b:
            a, b = b, a
        if f(a) * f(b) < 0:
            return a, b

def bisection(f, a, b, tol=1e-5, max_iter=100):
    midpoints = []
    values = []

    for _ in range(max_iter):
        c = (a + b) / 2
        midpoints.append(c)
        values.append(f(c))
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return np.array(midpoints), np.array(values)

f = get_polynomial()
a, b = find_initial_interval(f)
print(f"Initial interval found: [{a:.4f}, {b:.4f}]")

midpoints, values = bisection(f, a, b)

plt.plot(range(len(midpoints)), midpoints, marker='o', label='Midpoint values')
plt.axhline(y=0, color='gray', linestyle='--')
plt.title("Bisection Method Convergence")
plt.xlabel("Iteration")
plt.ylabel("Midpoint (x value)")
plt.grid(True)
plt.legend()
plt.show()
