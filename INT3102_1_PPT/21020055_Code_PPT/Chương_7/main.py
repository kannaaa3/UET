import IntegralApprox
from math import pi, e

if __name__ == "__main__":
    f = lambda x: (2 * pi) ** 0.5 * e ** (-x**2/2)
    a, b = (0, 1)
    n = 50

    trap = IntegralApprox.TrapezoidalRule()
    mid = IntegralApprox.MidpointRule()
    simp = IntegralApprox.SimpsonRule()

    print("Trapezoidal Rule: ", trap.solve(f, a, b, n))
    print("Midpoint Rule: ", mid.solve(f, a, b, n))
    print("Simpson Rule: ", simp.solve(f, a, b, n))
    


