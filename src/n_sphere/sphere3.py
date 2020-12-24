import math

import numexpr as ne
import numpy as np

from .sphere import sphere
from .vdcorput import vdcorput

# __x = np.linspace(0, math.pi, 300)  # NOQA
# __t = ne.evaluate('(__x - sin(__x) * cos(__x)) / 2')


# def sphere3_co(k, b):
#     """Generate Sphere-3 Halton sequence 0,..,k

#     Arguments:
#         k (int): maximum sequence index, non-negative integer

#     Keyword Arguments:
#         b ([int]): sequence base, integer exceeding 1

#     Returns:
#         ([float]): base-b low discrepancy sequence
#     """
#     assert len(b) >= 3

#     range_t = 0.5 * math.pi
#     sphere2_co = sphere_co(k, b[1:])
#     for vd in vdcorput_co(k, b[0]):
#         ti = range_t * vd  # map to [0, math.pi/2]
#         xi = np.interp(ti, __t, __x)
#         # xi = interp1(t, x, ti, 'spline')
#         cosxi = math.cos(xi)
#         sinxi = math.sin(xi)
#         yield [cosxi] + [sinxi * xi for xi in next(sphere2_co)]


class sphere3:
    """Generate Sphere-3 Halton sequence

    Arguments:
        k (int): maximum sequence index, non-negative integer

    Keyword Arguments:
        b ([int]): sequence base, integer exceeding 1

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    def __init__(self, b):
        assert len(b) >= 3
        self.range_t = 0.5 * math.pi
        self.sphere2 = sphere(b[1:])
        self.vdc = vdcorput(b[0])
        self.x = x = np.linspace(0, math.pi, 300)  # NOQA
        self.t = ne.evaluate('(x - sin(x) * cos(x)) / 2')

    def __next__(self):
        """Get the next item

        Returns:
            list:  the next item
        """
        vd = next(self.vdc)
        ti = self.range_t * vd  # map to [0, math.pi/2]
        xi = np.interp(ti, self.t, self.x)
        # xi = interp1(t, x, ti, 'spline')
        cosxi = math.cos(xi)
        sinxi = math.sin(xi)
        return [cosxi] + [sinxi * xi for xi in next(self.sphere2)]


# def sphere3_hopf_co(k, b):
#     """
#      sphere3_hopf   Halton sequence
#      INPUTS   : k - maximum sequence index, non-negative integer
#                 b - sequence base, integer exceeding 1
#     """
#     assert len(b) >= 3
#     vdc0 = vdcorput_co(k, b[0])
#     vdc1 = vdcorput_co(k, b[1])
#     twopi = 2 * math.pi
#     # fourpi = 4 * math.pi

#     for vd2 in vdcorput_co(k, b[2]):
#         phi = twopi * next(vdc0)  # map to [0, 2*math.pi]
#         psy = twopi * next(vdc1)  # map to [0, 2*math.pi]
#         z = 2 * vd2 - 1  # map to [-1., 1.]
#         eta = math.acos(z) / 2
#         cos_eta = math.cos(eta)
#         sin_eta = math.sin(eta)
#         yield [
#             cos_eta * math.cos(psy), cos_eta * math.sin(psy),
#             sin_eta * math.cos(phi + psy),
#             sin_eta * math.sin(phi + psy)
#         ]


class sphere3_hopf:
    """
     sphere3_hopf   Halton sequence
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
    """
    def __init__(self, b):
        assert len(b) >= 3
        self.b = b
        self.vdc0 = vdcorput(b[0])
        self.vdc1 = vdcorput(b[1])
        self.vdc2 = vdcorput(b[2])
        self.twopi = 2 * math.pi

    def __next__(self):
        """Get the next item

        Returns:
            list:  the next item
        """
        vd2 = next(self.vdc2)
        phi = self.twopi * next(self.vdc0)  # map to [0, 2*math.pi]
        psy = self.twopi * next(self.vdc1)  # map to [0, 2*math.pi]
        z = 2 * vd2 - 1  # map to [-1., 1.]
        eta = math.acos(z) / 2
        cos_eta = math.cos(eta)
        sin_eta = math.sin(eta)
        return [
            cos_eta * math.cos(psy), cos_eta * math.sin(psy),
            sin_eta * math.cos(phi + psy),
            sin_eta * math.sin(phi + psy)
        ]


if __name__ == "__main__":
    b = [2, 3, 5]

    spgen_hopf = sphere3_hopf(b)
    for _ in range(10):
        print(next(spgen_hopf))

    spgen = sphere3(b)
    for _ in range(10):
        print(next(spgen))
