def secantMethod(f, a: float, b: float,  tol=1e-6, max_iter=100):
    """
    Finding the root of function f(x) = 0 within [a..b] using secant method.
    """

    p0 = a
    p1 = b

    for i in range(max_iter):
        fp0 = f(p0)
        fp1 = f(p1)

        # Root found!
        if abs(fp0) < tol:
            return p0
        if abs(fp1 - fp0) < tol:
            print("Too close!")
            return None

        next_p = p1 - fp1 * (p1 - p0) / (fp1 - fp0)
        p0 = p1
        p1 = next_p

    print("Max Iteration Reached!")
    return None
