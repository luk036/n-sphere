import math

from .vdcorput import vdcorput


def circle(k, base=2):
    """Generate Circle Halton sequence 0,..,k

    Arguments:
        k (int): maximum sequence index, non-negative integer

    Keyword Arguments:
        base (int): [description] (default: {2})

    Returns:
        (list(float)): base-b low discrepancy sequence
    """
    for vd in vdcorput(k, base):
        theta = 2 * math.pi * vd  # map to [0, 2*math.pi]
        s = [math.cos(theta), math.sin(theta)]
        yield s


def sphere(k, b):
    """Generate Sphere Halton sequence 0,..,k

    Arguments:
        k (int): maximum sequence index, non-negative integer

    Keyword Arguments:
        b (list(int)): sequence base, integer exceeding 1

    Returns:
        (list(float)): base-b low discrepancy sequence
    """
    assert len(b) >= 2

    cirgen = circle(k, b[1])
    for vd in vdcorput(k, b[0]):
        cosphi = 2 * vd - 1  # map to [-1, 1]
        sinphi = math.sqrt(1 - cosphi * cosphi)
        c = next(cirgen)
        s = [cosphi, sinphi * c[0], sinphi * c[1]]
        yield s


if __name__ == "__main__":
    for c in circle(10, 2):
        print(c)

    for s in sphere(10, [2, 3]):
        print(s)
