def diff(f, x: float,  tol: float) -> float:
    """
    Return the derivative of function f at a specific point
    """
    return (f(x + tol) - f(tol)) / tol


def partial_diff(f, x: list, id: int, tol: float) -> float:
    """
    Return partial difference of function f at point x_id
    """
    f0 = f
    for i in range(len(x)):
        f = f(x[i])
        if i == id:
            f0 = f0(x[i] + tol)
        else:
            f0 = f0(x[i])
    return (f0 - f) / tol


# Bai toan thuan
def cumulative_error_direct_solver(f, x, x_abs_err, tol: float) -> float:
    """
    Solve the Direct Problem:
    Find absolute error of y = f(x), known x and absolute error of x.
    f : The function
    x : Can be a single float number if f is 1-variable, or a list of float
        numbers if f is multi-variable
    x_abs_err: Can be a single float number if f is 1-variable, or a list
        of float numbers if f is multi-variable
    tol: tolerance
    """
    if (type(x) == float):
        x = [x]
        x_abs_err = [x_abs_err]

    res = 0
    for i in range(len(x)):
        res += abs(diff(f, x[i], tol)) * x_abs_err[i]
    return res


# Bai toan nguoc
def cumulative_error_inverse_solver(f, x, y_abs_err, tol: float):
    """
    Solve the Inverse Problem:
    Find the bound for absolute error of x, known x and abs error of y = f(x).
    f : The function
    x : Can be a single float number if f is 1-variable, or a list of float
        numbers if f is multi-variable
    y_abs_err: a single float number, describe absolute error of y = f(x)
    tol: tolerance

    If f is 1-variable, return a single float that is the upper bound of
        absolute of x,
    otherwise, return a list consisting of n float numbers.
    """
    if (type(x) == float):
        return y_abs_err / diff(f, x, tol)

    res = list()
    n = len(x)
    for i in range(len(x)):
        res.append(y_abs_err / (n * partial_diff(f, x, i, tol)))
    return res
