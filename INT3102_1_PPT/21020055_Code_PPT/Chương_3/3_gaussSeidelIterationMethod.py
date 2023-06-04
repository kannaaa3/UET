import numpy as np
from numpy.linalg import inv, norm


def pNorm(A):
    """
    Return L_inf (p-norm) of a matrix.
    """
    return norm(A, np.inf)


def gaussSeidel(A: np.ndarray, b: np.ndarray, tol=1e-3) -> np.ndarray:
    """
        Return Numpy array of n [x_0, x_1, ..., x_n]
        Solve linear equation Ax = B using Gauss-Seidel method
    """

    L = np.tril(A, -1)
    U = np.triu(A, 1)
    I = np.identity(len(A))

    print("L = \n", L)
    print("U = \n", U)
    print("I = \n", I)

    C = -np.matmul(inv(I + L), U)
    d = np.matmul(inv(I + L), b)

    # if C is not convergent
    if (pNorm(C) > 1):
        print("Look! ", pNorm(C))
        raise Exception("Not satisfy condition for convergence!")

    print("C = \n", C)
    print("d = \n", d)

    maxDiff = 0
    x0 = d
    while True:
        x = np.matmul(C, x0) + d
        if (norm(x - x0) < maxDiff and norm(x-x0) < tol):
            break
        maxDiff = max(maxDiff, norm(x-x0))
        x0 = x

    return x.flatten()


def solve(A, b):
    """
    Convert 2d list A into a 2d array with diagonal full of 1.
    """
    for i in range(len(A)):
        div = A[i][i]
        for j in range(len(A)):
            A[i][j] = A[i][j] / div
        b[i][0] /= div
    print("A = \n", np.array(A))
    print("b =\n", np.array(b))

    return gaussSeidel(np.array(A), np.array(b))


if __name__ == "__main__":

    print("Exercise 8.")

    problems = [
        # a
        ([
            [4, 1, -1],
            [-1, 3, 1],
            [2, 2, 5]],
            [[5], [-4], [1]]),
        # b
        ([
            [-2, 1, 0.5],
            [1, -2, -0.5],
            [0, 1, 2]],
            [[4], [-4], [0]]),
        # c
        ([
            [4, 1, -1, 1],
            [1, 4, -1, -1],
            [-1, -1, 5, 1],
            [1, -1, 1, 3]],
            [[-2], [-1], [0], [1]]),
        # d
        ([[4, -1, 0, -1, 0, 0],
            [-1, 4, -1, 0, -1, 0],
            [0, -1, 4, 0, 0, -1],
            [-1, 0, 0, 4, -1, 0],
            [0, -1, 0, -1, 4, -1],
            [0, 0, -1, 0, -1, 4]],
         [[0], [5], [0], [6], [-2], [-6]]),

        ([[4, 1, -1],
         [-1, 3, 1],
            [2, 2, 5]],
         [[5], [-4], [1]])

    ]

    for i in range(len(problems)):
        print(chr(ord('a') + i),
              "-------------------------------------------------")
        A, b = problems[i]
        print("Solution x =", solve(A, b))

    # print(mGaussSeidel(A, b, TOL))
