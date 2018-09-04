def sphere3(k,b):
    # 2sphere   Base-b Halton elements 0,..,k
    # INPUTS   : k - maximum sequence index, non-negative integer
    #            b - sequence base, integer exceeding 1
    theta = 2*math.pi*vdcorput(k,b[0])           # map to [0, 2*math.pi]
    cosphi = 2*vdcorput(k,b[1]) - 1         # map to [-1, 1]
    sinphi = math.sqrt(1 - cosphi**2)
    x = [0:0.01:math.pi]
    t = -0.5*math.sin(x)*math.cos(x) + 0.5*x
    ti = 0.5*math.pi*vdcorput(k,b[2])            # map to [0, math.pi/2]
    xi = interp1(t,x,ti,'spline')
    cosxi = math.cos(xi)
    sinxi = math.sin(xi)
    s = [cosxi,
         sinxi*cosphi,
         sinxi*sinphi*math.cos(theta),
         sinxi*sinphi*math.sin(theta)]
    return s
    	 