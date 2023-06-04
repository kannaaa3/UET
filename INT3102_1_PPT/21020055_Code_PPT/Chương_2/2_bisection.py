from numpy import log2


def bisectionMethod(f, a: float, b: float, tol: float) -> float:
    """
    Finding the root of function f(x) = 0 within [a..b] using bisection method.
    """
    n0 = log2((b - a)/tol)
    i = 0
    p = 0
    while i < n0:
        p = (a + b) * 0.5
        print(a, p, b)
        if (f(p) * f(a) < 0):
            b = p
        else:
            a = p
        i += 1
    return p
