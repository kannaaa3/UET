import pprint
import numpy as np
from numpy import matmul
from numpy.linalg import inv
import scipy
import scipy.linalg


def LU_factorization(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve Ax = b precisely using LU factorization.
    Return an array of x_1, x_2, ..., x_n
    """
    _, L, U = scipy.linalg.lu(A)

    print("A:")
    pprint.pprint(A)

    print("L:")
    pprint.pprint(L)

    print("U:")
    pprint.pprint(U)

    y = matmul(inv(L), b)
    print(inv(L))
    pprint.pprint(y)

    x = matmul(inv(U), y)
    pprint.pprint(x)

    return x.flatten()


if __name__ == "__main__":
    A = np.array([[7, 3, -1, 2], [3, 8, 1, -4],
                  [-1, 1, 4, -1], [2, -4, -1, 6]])
    b = np.array([[1], [4], [2], [3]])
    print(LU_factorization(A, b))
