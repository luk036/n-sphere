def sphere(k,b):
    """
    2sphere   Base-b Halton elements 0,..,k
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence bases, integer exceeding 1
     OUTPUTS  : s - (k+1)*3 array, with s(i) storing element (i+1)
                    of base-b low discrepancy sequence
    """
    theta = 2*math.pi*vdcorput(k,b[0])           # map to [0, 2*math.pi]
    cosphi = 2*vdcorput(k,b[1]) - 1         # map to [-1, 1]
    sinphi = math.sqrt(1 - cosphi**2)
    s = [math.cos(theta)*sinphi, math.sin(theta)*sinphi, cosphi]
    #plot3(s(:,1), s(:,2), s(:,3), '+')
    return s
    