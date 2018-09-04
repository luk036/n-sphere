import math
import numpy as np

def vdc(n, base=2):
    vdc, denom = 0.0, 1.0
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder / denom
    return vdc


def vdcorput(n, base=2):
    '''
    n - number of vectors
    base - seeds
    '''
    for i in range(n):
        yield vdc(i, base)


def sphere(k, b):
    """
    2sphere   Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence bases, integer exceeding 1
     OUTPUTS  : s - (k+1)*3 array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    vd = zip(vdcorput(k, b[0]), vdcorput(k, b[1]))
    for vd0, vd1 in vd:
        theta = 2*math.pi*vd0      # map to [0, 2*math.pi]
        cosphi = 2*vd1 - 1         # map to [-1, 1]
        sinphi = math.sqrt(1 - cosphi**2)
        s = math.cos(theta)*sinphi, math.sin(theta)*sinphi, cosphi
        # plot3(s(:,1), s(:,2), s(:,3), '+')
        yield s


def sphere3_hopf(k, b):
    """
     sphere3_hopf   Halton sequence
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
    """
    vd = zip(vdcorput(k, b[0]), vdcorput(k, b[1]), vdcorput(k, b[2]))
    for vd0, vd1, vd2 in vd:
        phi = 2*math.pi*vd0   # map to [0, 2*math.pi]
        psy = 4*math.pi*vd1   # map to [0, 4*math.pi]
        z = 2*vd2 - 1         # map to [-1., 1.]
        theta = math.acos(z)
        cos_eta = math.cos(theta/2)
        sin_eta = math.sin(theta/2)
        s = [cos_eta * math.cos(psy/2),
            cos_eta * math.sin(psy/2),
            sin_eta * math.cos(phi + psy/2),
            sin_eta * math.sin(phi + psy/2)]
        yield s


def sphere3(k, b):
    """
     2sphere   Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
    """
    x = np.linspace(0,math.pi,3*k) # ???
    t = (x - np.sin(x)*np.cos(x)) / 2

    vd = zip(vdcorput(k, b[0]), vdcorput(k, b[1]), vdcorput(k, b[2]))
    for vd0, vd1, vd2 in vd:
        theta = 2*math.pi*vdcorput(k, b[0])        # map to [0, 2*math.pi]
        cosphi = 2*vdcorput(k, b[1]) - 1         # map to [-1, 1]
        sinphi = math.sqrt(1 - cosphi**2)
        ti = 0.5*math.pi*vd2         # map to [0, math.pi/2]
        xi = np.interp(ti, x, t)
        # xi = interp1(t, x, ti, 'spline')
        cosxi = math.cos(xi)
        sinxi = math.sin(xi)
        s = [cosxi,
            sinxi*cosphi,
            sinxi*sinphi*math.cos(theta),
            sinxi*sinphi*math.sin(theta)]
        yield s


def sphere_n(k, n, b):
    """ 
    n-sphere Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
     OUTPUTS  : s - (k+1)*(n+1) array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    x0 = 2*math.pi*vdcorput(k, b[0])           # map to [0, 2*math.pi]
    p = [math.cos(x0), math.sin(x0)]
    m = 3*k  # number of interpolation points???
    x = math.linspace(0,math.pi,m)
    for i in range(1, n):
        syms a
        t = subs(int(math.sin(a) ^ i), x)
        ti = t[0] + (t[m-1] - t[0]) * vdcorput(k, b[i])  # map to [t0, tm-1]
        xi = interp1(t, x, ti, 'spline')
        p = [math.cos(xi), math.sin(xi)*ones(1, i+1) * p]
    end
    return p
