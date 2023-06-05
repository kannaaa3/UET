import numpy as np
from math import comb


def newtonForwardDifference(givenPoint, x: np.ndarray, y: np.ndarray):
    n = len(x)
    res = 0
    difF = np.zeros((n, n))

    for j in range(n):
        difF[j][0] = y[j]

    for i in range(1, n):
        for j in range(n-i):
            difF[j][i] = difF[j+1][i-1] - difF[j][i-1]

    h = x[1] - x[0]
    r = (givenPoint - x[0])/h
    co = 1
    for i in range(n):
        res += difF[0][i] * co
        co *= (r - i) / (i+1)

    return res


if __name__ == "__main__":
    x = np.array([-0.75, -0.5, -0.25, 0])
    y = np.array([-0.0718125, -0.02475, 0.3349375, 0.2484244])
    print(newtonForwardDifference(-0.3333333, x, y))
