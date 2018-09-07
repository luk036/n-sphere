import math
from .vdcorput import vdcorput


def circle(k, base=2):
    """
    Circle   Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence bases, integer exceeding 1
     OUTPUTS  : s - (k+1)*3 array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    for vd in vdcorput(k, base):
        theta = 2*math.pi*vd      # map to [0, 2*math.pi]
        s = [math.cos(theta), math.sin(theta)]
        yield s


def sphere(k, b):
    """
    2sphere   Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence bases, integer exceeding 1
     OUTPUTS  : s - (k+1)*3 array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    assert len(b) >= 2

    cirgen = circle(k, b[1])
    for vd in vdcorput(k, b[0]):
        cosphi = 2*vd - 1         # map to [-1, 1]
        sinphi = math.sqrt(1 - cosphi*cosphi)
        c = next(cirgen)
        s = [cosphi, sinphi*c[0], sinphi*c[1]]
        yield s


if __name__ == "__main__":
    for c in circle(10, 2):
        print(c)

    for s in sphere(10, [2, 3]):
        print(s)
