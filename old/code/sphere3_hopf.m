function[s] = sphere3_hopf(k,b)
% sphere3_hopf   Halton sequence
% INPUTS   : k - maximum sequence index, non-negative integer
%            b - sequence base, integer exceeding 1
phi = 2*pi*vdcorput(k,b(1));   % map to [0, 2*pi]
psy = 4*pi*vdcorput(k,b(2));   % map to [0, 4*pi]
z = 2*vdcorput(k,b(3)) - 1;    % map to [-1, 1]
theta = acos(z);
cos_eta = cos(theta/2);
sin_eta = sin(theta/2);

s = [cos_eta .* cos(psy/2), ...
     cos_eta .* sin(psy/2), ...
     sin_eta .* cos(phi + psy/2), ...
     sin_eta .* sin(phi + psy/2)];

	 