from pytest import approx

import numpy as np
from scipy.spatial import ConvexHull

from n_sphere.discrep_2 import discrep_2
from n_sphere.sphere_n import cylin_n, sphere_n


def run_sphere(spgen):
    npoints = 600
    Triples = np.array([next(spgen) for _ in range(npoints)])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    return discrep_2(triangles, Triples)


def test_sphere_n():
    spgen = sphere_n(4, [2, 3, 5, 7])
    measure = run_sphere(spgen)
    assert measure == approx(0.9125914)
    # assert measure < 0.913
    # assert measure > 0.912


def test_cylin_n():
    cygen = cylin_n(4, [2, 3, 5, 7])
    measure = run_sphere(cygen)
    assert measure == approx(1.0505837105828988)
    # assert measure < 1.086
    # assert measure > 1.085
