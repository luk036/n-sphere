from scipy.spatial import ConvexHull
import numpy as np
from n_sphere.sphere3 import sphere3, sphere3_hopf
from n_sphere.discrep_2 import discrep_2


def test_sphere():
    npoints = 600
    Triples = np.array([p for p in sphere3(npoints, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure < 0.6502
    assert measure > 0.6501


def test_sphere_hopf():
    npoints = 600
    Triples = np.array([p for p in sphere3_hopf(npoints, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure < 0.7409
    assert measure > 0.7408
