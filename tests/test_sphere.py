from pytest import approx

import numpy as np
from scipy.spatial import ConvexHull

from n_sphere.discrep_2 import discrep_2
from n_sphere.sphere import sphere


def test_sphere():
    npoints = 600
    Triples = np.array([p for p in sphere(npoints, [2, 3, 5])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure == approx(0.2883404521)
    # assert measure < 0.2884
    # assert measure > 0.2883
