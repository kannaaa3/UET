import numpy as np
from math import exp


def f(x, y: np.ndarray):
    ans = np.ndarray(2)
    # ans[0] = y[2]
    # ans[1] = -y[1] - 2 * exp(x) + 1
    # ans[2] = -y[1] - exp(x) + 1
    ans[0] = y[0] - y[1] + 2
    ans[1] = -y[0] + y[1] + 4 * x
    # print("y0 =", y[0], "y1 =", y[1])
    return ans


def RK4(y: np.ndarray, x0: float, x1: float, h: float):
    """
    Return
    """
    iteration = 0
    while x0 <= x1 + h:
        print("# i = ", iteration, ":", sep="")
        k1 = f(x0, y)
        print("k1 = ", k1)
        k2 = f(x0 + 0.5 * h, y + 0.5 * h * k1)
        print("k2 = ", k2)
        k3 = f(x0 + 0.5 * h, y + 0.5 * h * k2)
        print("k3 = ", k3)
        k4 = f(x0 + h, y + h * k3)
        print("k4 = ", k4)

        print("x = ", x0, ", y = ", y)

        y = y + h/6 * (k1 + 0.5 * k2 + 0.5 * k3 + k4)
        x0 += h

        iteration += 1


if __name__ == "__main__":
    y = np.array([-1.0, 0])
    RK4(y, 0, 0.2, 0.1)
