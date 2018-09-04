function[p] = sphere_n(k,n,b)
% n-sphere Base-b Halton elements 0,..,k
% INPUTS   : k - maximum sequence index, non-negative integer
%            b - sequence base, integer exceeding 1
% OUTPUTS  : s - (k+1)*(n+1) array, with s(i) storing element (i+1)
%                of base-b low discrepancy sequence
x0 = (2*pi)*vdcorput(k,b(1));           % map to [0, 2*pi]
p = [cos(x0), sin(x0)];
m = 3*k; % number of interpolation points
x = [0:pi/(m-1):pi];
for i=1:n-1
   syms a;
   t = subs(int(sin(a)^i), x);
   ti = t(1) + (t(m) - t(1)) * vdcorput(k,b(i+1)); % map to [t1, tm]
   xi = interp1(t,x,ti,'spline');
   p = [cos(xi), sin(xi)*ones(1,i+1) .* p];
end
