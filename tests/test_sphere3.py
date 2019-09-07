from pytest import approx

import numpy as np
from scipy.spatial import ConvexHull

from n_sphere.discrep_2 import discrep_2
from n_sphere.sphere3 import sphere3, sphere3_hopf


def test_sphere():
    npoints = 600
    Triples = np.array([p for p in sphere3(npoints, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure == approx(0.65015)
    # assert measure < 0.6502
    # assert measure > 0.6501


def test_sphere_hopf():
    npoints = 600
    Triples = np.array([p for p in sphere3_hopf(npoints, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure == approx(0.740866)
    # assert measure < 0.7409
    # assert measure > 0.7408
