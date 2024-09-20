import numpy as np

class Integrator:
    def __init__(self, func=lambda x: x ** 3, n=100000):
        self.n = n
        self.func = func

    def integral(self, x1: float, x2: float, integrand) -> float:
        dx = (x2 - x1) / self.n
        x = np.linspace(x1 + dx / 2, x2 - dx / 2, self.n)
        y = integrand(x)
        return np.sum(y) * dx

    def erf(self, x2: float) -> float:
        def erf_integrand(x):
            return np.exp(-x ** 2)

        dx = x2 / self.n
        x = np.linspace(dx / 2, x2 - dx / 2, self.n)
        y = erf_integrand(x)
        return np.sum(y) * dx * 2 / np.sqrt(np.pi)

    def expval(self, x1: float, x2: float) -> float:
        def integrand(x):
            return self.func(x) * x


        total_val = self.integral(x1, x2, self.func)
        integral_val = self.integral(x1, x2, integrand)
        return  integral_val / total_val

    def variance(self, x1: float, x2: float) -> float:
        def variance_integrand(x):
            return self.func(x) * x ** 2

        variance_integral = self.integral(x1, x2, variance_integrand)

        total_integral = self.integral(x1, x2, self.func)

        return variance_integral / total_integral - self.expval(x1, x2) ** 2

    def std(self, x1: float, x2: float) -> float:
        return np.sqrt(self.variance(x1, x2))


class Differentiator:
    def __init__(self, tar_func, n=1000000):
        self.tar_func = tar_func
        self.n = n
    @staticmethod
    def ord_derivative(tar_func, x) -> float:
        der = (tar_func(x+0.001)-tar_func(x))/0.001
        return der