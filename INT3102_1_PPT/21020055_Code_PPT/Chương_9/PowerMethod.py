import numpy as np
from numpy.linalg import norm
from math import sqrt

class PowerMethodSolver():
    def solve(self, A: np.ndarray, x: np.ndarray, iter=100):
        """
            Computes the dominant eigenvalue and corresponding eigenvector
            of the given matrix A and initial vector x.
        """
        return None
    
    def norm(self, A: np.ndarray):
        """
        return norm
        """
        sum = 0
        for x in A:
            sum += x**2
        return sqrt(sum)

class EuclideanScaling(PowerMethodSolver):
    def solve(self, A: np.ndarray, x: np.ndarray, iter=100):
        for _ in range(iter):
            Ax = np.matmul(A, x)
            x = Ax / norm(Ax)
            eigenvalue = np.dot(Ax, x)
        return (eigenvalue, x)

class MaximumEntryScaling(PowerMethodSolver):
    def solve(self, A: np.ndarray, x: np.ndarray, iter=100):
        for _ in range(iter):
            Ax = np.matmul(A, x)
            x = Ax / max (Ax)
            eigenvalue = np.dot(Ax, x) / np.dot(x, x)
        return (eigenvalue, x)
    
if __name__ == "__main__":
    s = EuclideanScaling()
    # A = [[5, -1], [-1, -1]]
    # x = [1, 0]
    A = [[3, 2], [2, 3]]
    x = [1, 0]
    print(s.solve(np.array(A), np.array(x), 50))


