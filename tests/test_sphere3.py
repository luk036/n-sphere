from pytest import approx

import numpy as np
from scipy.spatial import ConvexHull

from n_sphere.discrep_2 import discrep_2
from n_sphere.sphere3 import sphere3, sphere3_hopf


def run_sphere(spgen):
    npoints = 600
    Triples = np.array([next(spgen) for _ in range(npoints)])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    return discrep_2(triangles, Triples)


def test_sphere():
    spgen = sphere3([2, 3, 5, 7])
    measure = run_sphere(spgen)
    assert measure == approx(0.6501446)
    # assert measure < 0.6502
    # assert measure > 0.6501


def test_sphere_hopf():
    spgen = sphere3_hopf([2, 3, 5, 7])
    measure = run_sphere(spgen)
    assert measure == approx(0.740866)
    # assert measure < 0.7409
    # assert measure > 0.7408
