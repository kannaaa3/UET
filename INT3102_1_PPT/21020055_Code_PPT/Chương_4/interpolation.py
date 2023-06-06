import numpy as np
from scipy.interpolate import CubicSpline
from math import prod

class Interpolation():
    def lagrangeInterpolation(self, f: list, givenPoint: float) -> float:
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

    def newton_forward(self, givenPoint, x: np.ndarray, y: np.ndarray):
        print("Newton Forward Difference Method:")
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
        co = 1 # Coefficient of Delta
        for i in range(n):
            res += difF[0][i] * co
            co *= (r - i) / (i+1)
        return res

    def cubic_spline(self,  x: np.ndarray, y: np.ndarray):
        print("Cubic Spline Method:")
        n = len(x)
        h = np.diff(x)

        # Calculate second derivatives
        alpha = np.zeros(n)
        for i in range(1, n-1):
            alpha[i] = (3/h[i])*(y[i+1]-y[i]) - (3/h[i-1])*(y[i]-y[i-1])
        
        l, mu, z = np.zeros(n), np.zeros(n), np.zeros(n)
        l[0] = 1
        mu[0] = z[0] = 0

        # Solve tridiagonal system
        for i in range(1, n-1):
            l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
            mu[i] = h[i] / l[i]
            z[i] = (alpha[i] - h[i-1]*z[i-1]) / l[i]

        l[n-1] = 1
        z[n-1] = 0
        c, b, d = np.zeros(n), np.zeros(n), np.zeros(n)

        # Calculate coefficients
        for j in range(n-2, -1, -1):
            c[j] = z[j] - mu[j] * c[j+1]
            b[j] = (y[j+1]-y[j]) / h[j] - h[j] * (c[j+1]+2*c[j]) / 3
            d[j] = (c[j+1] - c[j]) / (3*h[j])

        # Return the coefficients of each cubic polynomial
        return y[:-1], b, c[:-1], d

    def cubic_spline_calculator(self, givenPoint, x: np.ndarray, y: np.ndarray):
        # Coefficients
        c = solver.cubic_spline(x, y)
        if givenPoint in x:
            id = np.where(x == givenPoint)[0][0]
            return y[id]

        for i in range(len(x)-2, -1, -1):
            if givenPoint >= x[i]:
                diff = givenPoint - x[i]
                print("Diff =", diff )
                self.default_cs(x, y, givenPoint)
                return c[0][i] + c[1][i] * diff + c[2][i] * diff**2 + c[3][i] * diff**3
                break
        return None

    def default_cs(self, x, y, x_new):
        f = CubicSpline(x, y, bc_type='natural')
        y_new = f(x_new)
        print(y_new)



if __name__ == "__main__":
# Example usage
    x = np.array([0, 1, 2, 3, 4])  # x-coordinates
    y = np.array([0, 1, 4, 9, 16])  # y-coordinates

    solver = Interpolation()

    print(solver.cubic_spline_calculator(2.1, x, y))
