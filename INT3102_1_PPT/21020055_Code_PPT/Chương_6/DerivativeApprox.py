from math import pi, e

class DerivativeApproximation():
    def approx(self, f, x0, h):
        print("3-point midpoint: ", self.midpoint_rule_3point(f, x0, h))
        print("3-point endpoint: ", self.endpoint_rule_3point(f, x0, h))
        print("5-point midpoint: ", self.midpoint_rule_5point(f, x0, h))
        print("5-point endpoint: ", self.endpoint_rule_5point(f, x0, h))
        print("Second derivative: ", self.snd_derivative(f, x0, h))

    def midpoint_rule_3point(self, f, x0, h):
        d =  (f(x0+h) - f(x0-h)) / (2.0*h)
        return d

    def endpoint_rule_3point(self, f, x0, h):
        d =  (-3*f(x0) + 4*f(x0+h) - f(x0+2*h)) / (2.0*h)
        return d

    def midpoint_rule_5point(self, f, x0, h):
        d = (f(x0-2*h) - 8*f(x0-h) + 8*f(x0+h) - f(x0+2*h)) / (12*h)
        return d

    def endpoint_rule_5point(self, f, x0, h):
        d = (-25*f(x0) + 48*f(x0+h) - 36*f(x0+2*h) + 16*f(x0+3*h) - 3*f(x0+4*h)) / (12.0*h)
        return d
    def snd_derivative(self, f, x0, h):
        d = h**(-2) * (f(x0-h) - 2*f(x0) + f(x0+h))
        return d

if __name__ == "__main__":
    f = lambda x: (2*pi)**(-0.5) * e**(-x**2/2)

    x = [0, 1, 2]  # Points defining the interval [0, 2]
    dx = DerivativeApproximation()

    dx.approx(f, x[1], 1)
