import math

from .vdcorput import vdcorput

# def circle_co(k, base=2):
#     """Generate Circle Halton sequence 0,..,k

#     Arguments:
#         k (int): maximum sequence index, non-negative integer

#     Keyword Arguments:
#         base (int): [description] (default: {2})

#     Returns:
#         ([float]): base-b low discrepancy sequence
#     """
#     twopi = 2 * math.pi
#     for vd in vdcorput_co(k, base):
#         theta = twopi * vd  # map to [0, 2*math.pi]
#         s = [math.cos(theta), math.sin(theta)]
#         yield s


class circle:
    """Generate Circle Halton sequence 0,..,k

    Arguments:
        k (int): maximum sequence index, non-negative integer

    Keyword Arguments:
        base (int): [description] (default: {2})

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    def __init__(self, base=2):
        self.vc = vdcorput(base)
        self.twopi = 2 * math.pi

    def __next__(self):
        """Get the next item

        Raises:
            StopIteration:  description

        Returns:
            list:  the next item
        """
        vd = next(self.vc)
        theta = self.twopi * vd  # map to [0, 2*math.pi]
        return [math.cos(theta), math.sin(theta)]


# def sphere_co(k, b):
#     """Generate Sphere Halton sequence 0,..,k

#     Arguments:
#         k (int): maximum sequence index, non-negative integer

#     Keyword Arguments:
#         b ([int]): sequence base, integer exceeding 1

#     Returns:
#         ([float]): base-b low discrepancy sequence
#     """
#     assert len(b) >= 2

#     cirgen = circle_co(k, b[1])
#     for vd in vdcorput_co(k, b[0]):
#         cosphi = 2 * vd - 1  # map to [-1, 1]
#         sinphi = math.sqrt(1 - cosphi * cosphi)
#         c = next(cirgen)
#         s = [cosphi, sinphi * c[0], sinphi * c[1]]
#         yield s


class sphere:
    """Generate Sphere Halton sequence 0,..,k

    Arguments:
        k (int): maximum sequence index, non-negative integer

    Keyword Arguments:
        b ([int]): sequence base, integer exceeding 1

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    def __init__(self, b):
        assert len(b) >= 2
        self.cirgen = circle(b[1])
        self.vdc = vdcorput(b[0])

    def __next__(self):
        """Get the next item

        Returns:
            list:  the next item
        """
        vd = next(self.vdc)
        cosphi = 2 * vd - 1  # map to [-1, 1]
        sinphi = math.sqrt(1 - cosphi * cosphi)
        c = next(self.cirgen)
        return [cosphi, sinphi * c[0], sinphi * c[1]]


if __name__ == "__main__":
    cirgen = circle(2)
    for _ in range(10):
        print(next(cirgen))

    sgen = sphere(10, [2, 3])
    for _ in range(10):
        print(sgen)
