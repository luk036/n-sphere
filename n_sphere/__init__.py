"""
N-Sphere
=====
"""

from __future__ import absolute_import

import sys
if sys.version_info[:2] < (2, 7):
    m = "Python 2.7 or later is required for NetworkX (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

# Release data
from n_sphere import release

# from n_sphere.oracles import *
from n_sphere.discrep_2 import discrep_2
from n_sphere.halton_n import halton_n
from n_sphere.sphere_n import sphere_n, cylin_n
from n_sphere.sphere import sphere
from n_sphere.sphere3 import sphere3, sphere3_hopf
from n_sphere.vdcorput import vdc, vdcorput

# from n_sphere.lsq_corr_ell import lsq_corr_poly, lsq_corr_bspline
