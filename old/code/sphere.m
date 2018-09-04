function[s] = sphere(k,b)
% 2sphere   Base-b Halton elements 0,..,k
% INPUTS   : k - maximum sequence index, non-negative integer
%            b - sequence bases, integer exceeding 1
% OUTPUTS  : s - (k+1)*3 array, with s(i) storing element (i+1)
%                of base-b low discrepancy sequence
theta = 2*pi*vdcorput(k,b(1));           % map to [0, 2*pi]
cosphi = 2*vdcorput(k,b(2)) - 1;         % map to [-1, 1]
sinphi = sqrt(1 - cosphi.^2);
s = [cos(theta).*sinphi, sin(theta).*sinphi, cosphi];
%plot3(s(:,1), s(:,2), s(:,3), '+')