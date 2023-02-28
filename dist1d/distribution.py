import numpy as np
import scipy.integrate as integrate

class Distribution:
    def __init__(self, un_pdf, a, b):
        self.un_pdf = un_pdf
        self.a = a
        self.b = b
        self.c = None
        self.x_grid = None
        self.u_grid = None

    def compute_c(self, a=None, b=None):
        if a is None:
            a = self.a
        if b is None:
            b = self.b
        self.c = integrate.quad(self.un_pdf, a, b)[0]

    def pdf(self, x):
        if self.c is None:
            self.compute_c()
        return self.un_pdf(x) / self.c

    def cdf(self, x):
        if np.issctype(type(x)):
            u = integrate.quad(self.pdf, self.a, x)[0]
        else:
            n = len(x)
            u = np.empty(n)
            for i in range(n):
                u[i] = self.cdf(x[i])
        return u

    def compute_grid(self, n=1000):
        self.x_grid = np.linspace(self.a, self.b, num=n)
        self.u_grid = self.cdf(self.x_grid)

    def ppf(self, u):
        if self.u_grid is None:
            self.compute_grid()
        if np.issctype(type(u)):
            j = np.argmin(np.abs(u - self.u_grid))
            x = self.x_grid[j]
        else:
            n = len(u)
            x = np.empty(n)
            for i in range(n):
                j = np.argmin(np.abs(u[i] - self.u_grid))
                x[i] = self.x_grid[j]
        return x
