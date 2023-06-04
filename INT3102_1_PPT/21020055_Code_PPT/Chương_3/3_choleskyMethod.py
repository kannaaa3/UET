import numpy as np


def isPositiveDefinite(A: np.ndarray):
    return np.all(np.linalg.eigvals(A) > 0)


def choleskyMethod(A: np.ndarray) -> np.ndarray:
    if not isPositiveDefinite(A):
        raise Exception("A is not positive definite matrix!")
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        sumSqr = np.sum(L[i][:i]**2)
        print(sumSqr)
        L[i][i] = np.sqrt(A[i][i] - sumSqr)

        for j in range(i, n):
            sumRow = 0
            for s in range(j):
                sumRow += L[i][s] * L[j][s]
            L[j][i] = (A[j][i] - sumRow) / L[i][i]

    return L


if __name__ == "__main__":
    A = np.array([
        [9, -3, -3],
        [-3, 10, 1],
        [3, 1, 5]])
    print(choleskyMethod(A))
