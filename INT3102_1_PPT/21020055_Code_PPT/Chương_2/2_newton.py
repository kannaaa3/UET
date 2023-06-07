def derivative(f, x: float, tol) -> float:
    """
    Return the derivative of function f at a specific point
    """
    return (f(x + tol) - f(x)) / tol


def newtonMethod(f, p0, tol=1e-3, max_iter=100):
    """
    Finding the root of function f(x) = 0 within [a..b] using Newton's method.
    """
    for i in range(max_iter):
        # Result found
        if abs(f(p0)) < tol:
            return p0

        df = derivative(f, p0, tol)
        if (df == 0):
            print("Error: Zero derivative at p0 =", p0)
            return None
        p0 = p0 - f(p0) / df

    print("Max Iteration Reached!")
    return None
