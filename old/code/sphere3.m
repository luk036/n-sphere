function[s] = sphere3(k,b)
% 2sphere   Base-b Halton elements 0,..,k
% INPUTS   : k - maximum sequence index, non-negative integer
%            b - sequence base, integer exceeding 1
theta = 2*pi*vdcorput(k,b(1));           % map to [0, 2*pi]
cosphi = 2*vdcorput(k,b(2)) - 1;         % map to [-1, 1]
sinphi = sqrt(1 - cosphi.^2);
x = [0:0.01:pi];
t = -0.5*sin(x).*cos(x) + 0.5*x;
ti = 0.5*pi*vdcorput(k,b(3));            % map to [0, pi/2]
xi = interp1(t,x,ti,'spline');
cosxi = cos(xi);
sinxi = sin(xi);
s = [cosxi, ...
     sinxi.*cosphi, ...
     sinxi.*sinphi.*cos(theta), ...
     sinxi.*sinphi.*sin(theta)];

	 