from pytest import approx

import numpy as np
from scipy.spatial import ConvexHull

from n_sphere.discrep_2 import discrep_2
from n_sphere.sphere_n import cylin_n, sphere_n


def test_sphere_n():
    npoints = 600
    Triples = np.array([p for p in sphere_n(npoints, 4, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure == approx(0.9125958)
    # assert measure < 0.913
    # assert measure > 0.912


def test_cylin_n():
    npoints = 600
    Triples = np.array([p for p in cylin_n(npoints, 4, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure == approx(1.085613578)
    # assert measure < 1.086
    # assert measure > 1.085
