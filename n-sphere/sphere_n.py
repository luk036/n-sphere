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
    return np.array([vdc(i, base) for i in range(n)])


def sphere(k, b):
    """
    2sphere   Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence bases, integer exceeding 1
     OUTPUTS  : s - (k+1)*3 array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    theta = 2*np.pi*vdcorput(k, b[0])           # map to [0, 2*np.pi]
    cosphi = 2*vdcorput(k, b[1]) - 1         # map to [-1, 1]
    sinphi = np.sqrt(1 - cosphi**2)
    s = [np.cos(theta)*sinphi, np.sin(theta)*sinphi, cosphi]
    # plot3(s(:,1), s(:,2), s(:,3), '+')
    return s


def sphere3_hopf(k, b):
    """
     sphere3_hopf   Halton sequence
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
    """
    phi = 2*np.pi*vdcorput(k, b[0])   # map to [0, 2*np.pi]
    psy = 4*np.pi*vdcorput(k, b[1])   # map to [0, 4*np.pi]
    z = 2*vdcorput(k, b[2]) - 1       # map to [-1, 1]
    theta = np.acos(z)
    cos_eta = np.cos(theta/2.)
    sin_eta = np.sin(theta/2.)

    s = [cos_eta * np.cos(psy/2.),
         cos_eta * np.sin(psy/2.),
         sin_eta * np.cos(phi + psy/2.),
         sin_eta * np.sin(phi + psy/2.)]

    return s


def sphere3(k, b):
    # 2sphere   Base-b Halton elements 0,..,k
    # INPUTS   : k - maximum sequence index, non-negative integer
    #            b - sequence base, integer exceeding 1
    theta = 2*np.pi*vdcorput(k, b[0])        # map to [0, 2*np.pi]
    cosphi = 2*vdcorput(k, b[1]) - 1         # map to [-1, 1]
    sinphi = np.sqrt(1 - cosphi**2)
    x = [0:0.01:np.pi]
    t = -0.5*np.sin(x)*np.cos(x) + 0.5*x
    ti = 0.5*np.pi*vdcorput(k, b[2])         # map to [0, np.pi/2.]
    xi = interp1(t, x, ti, 'spline')
    cosxi = np.cos(xi)
    sinxi = np.sin(xi)
    s = [cosxi,
         sinxi*cosphi,
         sinxi*sinphi*np.cos(theta),
         sinxi*sinphi*np.sin(theta)]
    return s


def sphere_n(k, n, b):
    """ 
    n-sphere Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
     OUTPUTS  : s - (k+1)*(n+1) array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    x0 = (2*np.pi)*vdcorput(k, b[0])           # map to [0, 2*np.pi]
    p = [np.cos(x0), np.sin(x0)]
    m = 3*k  # number of interpolation points
    x = [0:np.pi/(m-1):np.pi]
    for i in range(1, n):
        syms a
        t = subs(int(np.sin(a) ^ i), x)
        ti = t[0] + (t[m-1] - t[0]) * vdcorput(k, b[i])  # map to [t1, tm]
        xi = interp1(t, x, ti, 'spline')
        p = [np.cos(xi), np.sin(xi)*ones(1, i+1) * p]
    end
    return p
