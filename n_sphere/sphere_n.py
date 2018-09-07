import math
import numpy as np
from .vdcorput import vdcorput
from .sphere3 import sphere3


def int_sin_power(n, x):
    if n == 0:
        return x
    if n == 1:
        return -np.cos(x)
    return ((n-1)*int_sin_power(n-2, x) - np.cos(x)*np.sin(x)**(n-1))/n


def sphere_n(k, n, b):
    """ 
    n_sphere Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
     OUTPUTS  : s - (k+1)*(n+1) array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    assert n >= 3
    assert len(b) >= n

    if n == 3:
        yield from sphere3(k, b)
        return

    m = 3*k  # number of interpolation points???
    x = np.linspace(0, math.pi, m)
    t = int_sin_power(n-1, x)
    range_t = t[-1] - t[0]
    S = sphere_n(k, n-1, b[1:])

    for vd in vdcorput(k, b[0]):
        ti = t[0] + range_t * vd  # map to [t0, tm-1]
        xi = np.interp(ti, t, x)
        cosxi = math.cos(xi)
        sinxi = math.sin(xi)
        s2 = sinxi * np.array(next(S))
        s = [cosxi] + s2.tolist()
        yield s


if __name__ == "__main__":
    b = [2, 3, 5, 7, 2]
    points = np.array([p for p in sphere_n(10, 3, b)])
    print(points[0]*4.0)
