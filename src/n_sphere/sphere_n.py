import math

import numexpr as ne
import numpy as np

from .sphere import circle, sphere
from .vdcorput import vdcorput


def int_sin_power(n, x):
    """Evaluate integral sin^n(x) dx

    Arguments:
        n (int): power
        x (float): [description]

    Returns:
        float: [description]
    """
    if n == 0:
        return x
    if n == 1:
        return -np.cos(x)
    Snm2 = int_sin_power(n - 2, x)  # NOQA
    return ne.evaluate('((n - 1) * Snm2 - cos(x) * sin(x)**(n - 1)) / n')


# def sphere_n_co(k, n, b):
#     """Generate n-sphere base-b Halton sequence 0,..,k

#     Arguments:
#         k (int): maximum sequence index, non-negative integer
#         n (int): [description]
#         b ([int]): sequence base, integer exceeding 1

#     Returns:
#         ([float]): base-b low discrepancy sequence
#     """
#     assert n >= 2
#     assert len(b) >= n

#     if n == 2:
#         for s in sphere_co(k, b):
#             yield s
#         return

#     m = 300  # number of interpolation points???
#     x = np.linspace(0, math.pi, m)
#     t = int_sin_power(n - 1, x)
#     range_t = t[-1] - t[0]
#     S = sphere_n_co(k, n - 1, b[1:])

#     for vd in vdcorput_co(k, b[0]):
#         ti = t[0] + range_t * vd  # map to [t0, tm-1]
#         xi = np.interp(ti, t, x)
#         cosxi = math.cos(xi)
#         sinxi = math.sin(xi)
#         yield [cosxi] + [sinxi * xi for xi in next(S)]


class sphere_n:
    """Generate Sphere-3 Halton sequence

    Arguments:
        k (int): maximum sequence index, non-negative integer

    Keyword Arguments:
        b ([int]): sequence base, integer exceeding 1

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    def __init__(self, n, b):
        assert n >= 3
        assert len(b) >= n

        m = 300  # number of interpolation points???
        self.x = np.linspace(0, math.pi, m)
        self.t = int_sin_power(n - 1, self.x)
        self.range_t = self.t[-1] - self.t[0]
        self.S = sphere(b[1:]) if n == 3 else sphere_n(n - 1, b[1:])
        self.vdc = vdcorput(b[0])

    def __next__(self):
        """Get the next item

        Returns:
            list:  the next item
        """
        vd = next(self.vdc)
        ti = self.t[0] + self.range_t * vd  # map to [t0, tm-1]
        xi = np.interp(ti, self.t, self.x)
        cosxi = math.cos(xi)
        sinxi = math.sin(xi)
        return [cosxi] + [sinxi * xi for xi in next(self.S)]


# def cylin_n_co(k, n, b):
#     """Generate using cylindrical coordinate method

#     Arguments:
#         k (int): maximum sequence index, non-negative integer
#         n (int): [description]
#         b ([int]): sequence base, integer exceeding 1

#     Returns:
#         ([float]): base-b low discrepancy sequence
#     """
#     assert n >= 1
#     assert len(b) >= n

#     if n == 1:
#         for s in circle_co(k, b[0]):
#             yield s
#         return

#     S = cylin_n_co(k, n - 1, b[1:])

#     for vd in vdcorput_co(k, b[0]):
#         cosphi = 2 * vd - 1  # map to [-1, 1]
#         sinphi = math.sqrt(1 - cosphi * cosphi)
#         yield [cosphi] + [sinphi * xi for xi in next(S)]


class cylin_n:
    """Generate using cylindrical coordinate method

    Arguments:
        k (int): maximum sequence index, non-negative integer
        n (int): [description]
        b ([int]): sequence base, integer exceeding 1

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    def __init__(self, n, b):
        assert n >= 1
        assert len(b) >= n
        self.S = circle(b[1]) if n == 2 else cylin_n(n - 1, b[1:])
        self.vdc = vdcorput(b[0])

    def __next__(self):
        """Get the next item

        Returns:
            list:  the next item
        """
        vd = next(self.vdc)
        cosphi = 2 * vd - 1  # map to [-1, 1]
        sinphi = math.sqrt(1 - cosphi * cosphi)
        return [cosphi] + [sinphi * xi for xi in next(self.S)]


if __name__ == "__main__":
    b = [2, 3, 5, 7, 11]

    spgen = sphere_n(3, b)
    for _ in range(10):
        print(next(spgen))

    cygen = cylin_n(3, b)
    for _ in range(10):
        print(next(cygen))
