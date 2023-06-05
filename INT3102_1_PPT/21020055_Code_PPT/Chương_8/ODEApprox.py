import numpy as np

class ODEApprox():
    def RK4(self, y: np.ndarray, x0: float, df,  h: float, iter=10):
        """
        y       - ODEs
        x0      - starting point
        df      - derivative function
        h       - step size
        """
        print("4th order Runge-Kutta method:")
        for i in range(iter):
            print("# i = ", i, ":", sep="", end=" ")
            k1 = df(x0, y)
            # print("k1 = ", k1)
            k2 = df(x0 + 0.5 * h, y + 0.5 * h * k1)
            # print("k2 = ", k2)
            k3 = df(x0 + 0.5 * h, y + 0.5 * h * k2)
            # print("k3 = ", k3)
            k4 = df(x0 + h, y + h * k3)
            # print("k4 = ", k4)



            y = y + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)

            print("x = ", x0, ", y = ", y)
            x0 += h
        print()

    def taylor_series_method(self, y: np.ndarray, x0: float, df, h: float, iter=10):
        print("Taylor Series Method:")
        for i in range(iter):
            print("# i = ", i, ":", sep="", end=" ")
            y = y + h * df(x0, y)
            print("y = ", y)
            x0 += h

        print()

    def midpoint_method(self, y: np.ndarray, x0: float, df, h: float, iter=10):
        print("Midpoint Method:")
        for i in range(iter):
            print("# i = ", i, ":", sep="" , end=" ")
            x_mid = x0 + h * 0.5
            y_mid = y + h * 0.5 * df(x0, y)
            f_mid = df(x_mid, y_mid)
            y = y + h * f_mid
            print("y =", y)
            x0 += h

        return 0

    def heun_method(self, y: np.ndarray, x0: float, df, h: float, iter=10):
        print("Heun Method:")
        for i in range(iter):
            print("# i = ", i, ":", sep="", end=" ")
            y_predict = y + h * df(x0, y)
            y = y + h * 0.5 * (df(x0 ,y) + df(x0 + h, y_predict))
            print("y =", y)
            x0 += h
    
# Config here
def f(x, y: np.ndarray):
    ans = np.ndarray(1)
    # ans[0] = y[2]
    # ans[1] = -y[1] - 2 * exp(x) + 1
    # ans[2] = -y[1] - exp(x) + 1

    # ans[0] = y[0] - y[1] + 2
    # ans[1] = -y[0] + y[1] + 4 * x
    ans[0] = 2 * x * y[0]
    return ans

if __name__ == "__main__":
    y = np.array([1])
    ode_a = ODEApprox()
    ode_a.taylor_series_method(y, 1, f, 0.01, 10)
    ode_a.midpoint_method(y, 1, f, 0.01, 10)
    ode_a.heun_method(y, 1, f, 0.01, 10)
    ode_a.RK4(y, 1, f, 0.01, 10)

    # for i in range(10):
    #     print(i, " & $", round(lst[i][0], 12), "$ & $", round(lst[i][1],12), "$ & $", round(lst[i][2], 12), "$ & $", round(lst[i][3], 12), "$ \\\\" )

