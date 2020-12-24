from .vdcorput import vdcorput

# def halton_n_co(k, n, b):
#     """Generate base-b Halton sequence 0,..,k

#     Arguments:
#         k (int): maximum sequence index, non-negative integer
#         n (int): [description]
#         b ([int]): sequence base, integer exceeding 1

#     Returns:
#         ([float]): base-b low discrepancy sequence
#     """
#     if n == 1:
#         for s in vdcorput_co(k, b[0]):
#             yield [s]
#         return

#     S = halton_n_co(k, n - 1, b[1:])

#     for vd in vdcorput_co(k, b[0]):
#         yield [vd] + next(S)


class halton:
    """Generate base-b Halton sequence

    Arguments:
        n (int): [description]
        b ([int]): sequence base, integer exceeding 1

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    def __init__(self, b):
        self.vdc0 = vdcorput(b[0])
        self.vdc0 = vdcorput(b[0])

    def __next__(self):
        """Get the next item

        Returns:
            list(float):  the next item
        """
        return [next(self.vdc0), next(self.vdc1)]


class halton_n:
    """Generate base-b Halton sequence

    Arguments:
        n (int): [description]
        b ([int]): sequence base, integer exceeding 1

    Returns:
        ([float]): base-b low discrepancy sequence
    """
    def __init__(self, n, b):
        assert n >= 3
        self.vdc = vdcorput(b[0])
        self.S = halton(b[1:]) if n == 3 else halton_n(n - 1, b[1:])

    def __next__(self):
        """Get the next item

        Returns:
            list(float):  the next item
        """
        return [next(self.vdc)] + next(self.S)


if __name__ == "__main__":
    b = [2, 3]

    hgen = halton([2, 3])
    for _ in range(10):
        print(next(hgen))

    hgen_n = halton_n(3, [2, 3, 5])
    for _ in range(10):
        print(next(hgen_n))
