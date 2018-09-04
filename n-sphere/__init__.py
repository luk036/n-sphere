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
from n-sphere import release

# from n-sphere.oracles import *
from n-sphere.cutting_plane import *
from n-sphere.ell import *
from n-sphere.problem import Problem

import n-sphere.oracles
from n-sphere.oracles import *
# from n-sphere.lsq_corr_ell import lsq_corr_poly, lsq_corr_bspline
