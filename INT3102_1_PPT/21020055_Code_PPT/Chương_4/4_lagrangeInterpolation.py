from math import prod


def lagrangeInterpolation(f: list, givenPoint: float) -> float:
    """
        Lagrange interpolation formula.
    """
    n = len(f)
    res = 0

    for i in range(n):
        lx = prod([givenPoint - f[j][0] for j in range(n) if j != i])
        lxi = prod([f[i][0] - f[j][0] for j in range(n) if j != i])
        res += lx / lxi * f[i][1]

    return res


if __name__ == "__main__":
    print("Example.", lagrangeInterpolation(
        [(0.698, 0.7661), (0.733, 0.7432), (0.768, 0.7193), (0.803, 0.6946)],
        0.75))
