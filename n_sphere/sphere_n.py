import math
import numpy as np
from .vdcorput import vdcorput
from .sphere import sphere, circle


def int_sin_power(n, x):
    """Evaluate $$\int sin^n(x) dx$$

    Arguments:
        n {int} -- power
        x {float} -- [description]

    Returns:
        float -- [description]
    """
    if n == 0:
        return x
    if n == 1:
        return -np.cos(x)
    return ((n-1)*int_sin_power(n-2, x) - np.cos(x)*np.sin(x)**(n-1))/n


def sphere_n(k, n, b):
    """Generate n-sphere base-b Halton sequence 0,..,k

    Arguments:
        k {int} -- maximum sequence index, non-negative integer
        n {int} -- [description]
        b {list(int)} -- sequence base, integer exceeding 1

    Returns:
        {list(float)} -- base-b low discrepancy sequence
    """
    assert n >= 2
    assert len(b) >= n

    if n == 2:
        for s in sphere(k, b):
            yield s
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


def cylin_n(k, n, b):
    """Generate using cylindrical coordinate method

    Arguments:
        k {int} -- maximum sequence index, non-negative integer
        n {int} -- [description]
        b {list(int)} -- sequence base, integer exceeding 1

    Returns:
        {list(float)} -- base-b low discrepancy sequence
    """
    assert n >= 1
    assert len(b) >= n

    if n == 1:
        for s in circle(k, b[0]):
            yield s
        return

    S = cylin_n(k, n-1, b[1:])

    for vd in vdcorput(k, b[0]):
        cosphi = 2*vd - 1         # map to [-1, 1]
        sinphi = math.sqrt(1 - cosphi*cosphi)
        s3 = sinphi * np.array(next(S))
        s = [cosphi] + s3.tolist()
        yield s


if __name__ == "__main__":
    b = [2, 3, 5, 7, 11]
    points = np.array([p for p in sphere_n(10, 3, b)])
    print(points)
    points = np.array([p for p in cylin_n(10, 3, b)])
    print(points)
