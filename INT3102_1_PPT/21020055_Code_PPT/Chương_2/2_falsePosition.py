def falsePosition(f, a: float, b: float, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x_intercept = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(x_intercept)
        if abs(fc) < tol:
            return x_intercept
        elif fc > 0:
            b = x_intercept
        else:
            a = x_intercept
    print("Maximum Iteration Reached!")
    return None
