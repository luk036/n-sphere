def sphere3_hopf(k,b):
    """
     sphere3_hopf   Halton sequence
     INPUTS   : k - maximum sequence index, non-negative integer
                b - sequence base, integer exceeding 1
    """
    phi = 2*math.pi*vdcorput(k,b[0])   # map to [0, 2*math.pi]
    psy = 4*math.pi*vdcorput(k,b[1])   # map to [0, 4*math.pi]
    z = 2*vdcorput(k,b[2]) - 1    # map to [-1, 1]
    theta = math.acos(z)
    cos_eta = math.cos(theta/2)
    sin_eta = math.sin(theta/2)
    
    s = [cos_eta * math.cos(psy/2),
         cos_eta * math.sin(psy/2),
         sin_eta * math.cos(phi + psy/2),
         sin_eta * math.sin(phi + psy/2)]
    
    return s