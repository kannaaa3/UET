class IntegralApproximation():
    def solve(self, f, a, b, n):
        """
        f: The function we'll be evaluating
        a       - Lower bound
        b       - Upper bound
        n       - Number of step
        """
        return None

class TrapezoidalRule(IntegralApproximation):
    def solve(self, f, a, b, n):
        h = (b - a) / n # Step size
        integral = 0 # The result

        integral += (f(a) + f(b)) / 2.0
        for i in range(1, n):
            x = a + i * h # Calculate x coordinate
            integral += f(x)

        integral *= h

        return integral

class MidpointRule(IntegralApproximation):
    def solve(self, f, a, b , n):
        h = (b - a) / n # Step size
        integral = 0

        for i in range(n-1):
            x = a + (i + 0.5) * h
            integral += f(x)

        integral *= h

        return integral

class SimpsonRule(IntegralApproximation):
    def solve(self, f, a, b, n):
        h = (b - a) / n # Step size
        integral = 0

        for i in range(n):
            x0 = a + i * h
            x1 = a + (i + 0.5) * h
            x2 = a + (i + 1) * h

            integral += f(x0) + 4 * f(x1) + f(x2)

        integral *= h/6

        return integral

