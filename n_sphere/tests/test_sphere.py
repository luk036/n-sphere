from pytest import approx

from scipy.spatial import ConvexHull
import numpy as np
from ..sphere import sphere
from ..discrep_2 import discrep_2


def test_sphere():
    npoints = 600
    Triples = np.array([p for p in sphere(npoints, [2, 3, 5])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure == approx(0.2883404521)
    # assert measure < 0.2884
    # assert measure > 0.2883
