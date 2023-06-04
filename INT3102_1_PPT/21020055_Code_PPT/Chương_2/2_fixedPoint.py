def fixedPointIteration(g, x: float, max_iter=100, tol=1e-6):
    """
    Finding the root of function f(x) = 0 within [a..b]
    using fixed-point iteration method.
    N: Maximum Iteration
    """
    for i in range(max_iter):
        if abs(x - g(x)) >= tol:
            return x
        x = g(x)
    print("Max Iteration Reached!")
    return None
