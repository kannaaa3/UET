import numpy as np
from numpy.linalg import inv, norm


def pNorm(A):
    """
    Return L_inf (p-norm) of a matrix.
    """
    return norm(A, np.inf)


def jacobiMethod(A: np.ndarray, x0: np.ndarray, b: np.ndarray,
                 tol=1e-3, max_iter=1000):
    """
        Return Numpy array of n [x_0, x_1, ..., x_n]
        Solve linear equation Ax = B using Gauss-Seidel method
    """

    I = np.identity(len(A))
    C = I + (-A)

    # if C is not convergent
    if (pNorm(C) > 1):
        print("Look! ", pNorm(C))
        raise Exception("Not satisfy condition for convergence!")

    print("I - A = \n", C)

    for i in range(max_iter):
        x = b + np.matmul(C, x0)
        if (norm(x-x0) < tol):
            return x.flatten()
        x0 = x

    return None


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

    x0 = np.zeros_like(b)

    return jacobiMethod(np.array(A), x0, np.array(b))


if __name__ == "__main__":

    print("Exercise 8.")

    problems = [
        # # a
        # ([
        #     [4, 1, -1],
        #     [-1, 3, 1],
        #     [2, 2, 5]],
        #     [[5], [-4], [1]]),
        # # b
        # ([
        #     [-2, 1, 0.5],
        #     [1, -2, -0.5],
        #     [0, 1, 2]],
        #     [[4], [-4], [0]]),
        # # c
        # ([
        #     [4, 1, -1, 1],
        #     [1, 4, -1, -1],
        #     [-1, -1, 5, 1],
        #     [1, -1, 1, 3]],
        #     [[-2], [-1], [0], [1]]),
        # # d
        # ([[4, -1, 0, -1, 0, 0],
        #     [-1, 4, -1, 0, -1, 0],
        #     [0, -1, 4, 0, 0, -1],
        #     [-1, 0, 0, 4, -1, 0],
        #     [0, -1, 0, -1, 4, -1],
        #     [0, 0, -1, 0, -1, 4]],
        #  [[0], [5], [0], [6], [-2], [-6]]),
        #
        # ([[4, 1, -1],
        #  [-1, 3, 1],
        #     [2, 2, 5]],
        #  [[5], [-4], [1]])
        ([[9, -3, -3],
          [-3, 10, 1],
          [-3, 1, 5]],
         [[-9], [-1.5], [5]])

    ]

    for i in range(len(problems)):
        print("\n", chr(ord('a') + i),
              "----------------------------------------------------------")
        A, b = problems[i]
        print("Solution x =", solve(A, b))

    # print(mGaussSeidel(A, b, TOL))
