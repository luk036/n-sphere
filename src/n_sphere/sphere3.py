import math

import numexpr as ne
import numpy as np

from .sphere import sphere
from .vdcorput import vdcorput


def sphere3(k, b):
    """Generate Sphere-3 Halton sequence 0,..,k

    Arguments:
        k (int): maximum sequence index, non-negative integer

    Keyword Arguments:
        b ([int]): sequence base, integer exceeding 1

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    assert len(b) >= 3

    x = np.linspace(0, math.pi, 3 * k)  # ???
    t = ne.evaluate('(x - sin(x) * cos(x)) / 2')
    range_t = 0.5 * math.pi
    sphere2 = sphere(k, b[1:])
    for vd in vdcorput(k, b[0]):
        ti = range_t * vd  # map to [0, math.pi/2]
        xi = np.interp(ti, t, x)
        # xi = interp1(t, x, ti, 'spline')
        cosxi = math.cos(xi)
        sinxi = math.sin(xi)
        s2 = sinxi * np.array(next(sphere2))
        s = [cosxi] + s2.tolist()
        yield s


def sphere3_hopf(k, b):
    """
     sphere3_hopf   Halton sequence
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
    """
    assert len(b) >= 3

    vd = zip(vdcorput(k, b[0]), vdcorput(k, b[1]), vdcorput(k, b[2]))
    for vd0, vd1, vd2 in vd:
        phi = 2 * math.pi * vd0  # map to [0, 2*math.pi]
        psy = 4 * math.pi * vd1  # map to [0, 4*math.pi]
        z = 2 * vd2 - 1  # map to [-1., 1.]
        theta = math.acos(z)
        cos_eta = math.cos(theta / 2)
        sin_eta = math.sin(theta / 2)
        s = [
            cos_eta * math.cos(psy / 2), cos_eta * math.sin(psy / 2),
            sin_eta * math.cos(phi + psy / 2),
            sin_eta * math.sin(phi + psy / 2)
        ]
        yield s


if __name__ == "__main__":
    b = [2, 3, 5]

    for h in sphere3_hopf(10, b):
        print(h)

    for s in sphere3(10, b):
        print(s)
