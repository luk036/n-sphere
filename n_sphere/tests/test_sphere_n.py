from scipy.spatial import ConvexHull
import numpy as np
from n_sphere.sphere_n import sphere_n, cylin_n
from n_sphere.discrep_2 import discrep_2


def test_sphere_n():
    npoints = 600
    Triples = np.array([p for p in sphere_n(npoints, 4, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure < 0.913
    assert measure > 0.912

def test_cylin_n():
    npoints = 600
    Triples = np.array([p for p in cylin_n(npoints, 4, [2, 3, 5, 7])])
    hull = ConvexHull(Triples)
    triangles = hull.simplices
    measure = discrep_2(triangles, Triples)
    assert measure < 1.086
    assert measure > 1.085
