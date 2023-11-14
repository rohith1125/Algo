import numpy as np

f = lambda x: x**3 - (1/10)
f_prime = lambda x: 3*(x**2)

def my_newton(f, df, x0, tol):
    if abs(f(x0)) < tol:
        return x0
    else:
        return my_newton(f, df, x0 - f(x0)/df(x0), tol)

estimate = my_newton(f, f_prime, 0.5, 1e-5)
print("estimate =", "{:.5f}".format(estimate))