function[s] = vdcorput(k,b)
% VDCORPUT   Base-b Van der Corput sequence, elements 0,..,k
% INPUTS   : k - maximum sequence index, non-negative integer
%            b - sequence base, integer exceeding 1
% OUTPUTS  : s - (k+1)*1 array, with s(i) storing element (i+1)
%                of base-b Van der Corput sequence
% EXAMPLE  : vdcorput(0,2) = 0
%            vdcorput(1,2) = [0 0.5]'
%            vdcorput(2,2) = [0 0.5 0.25]'
% AUTHOR   : Dimitri Shvorob, dimitri.shvorob@vanderbilt.edu, 6/20/07
if k ~= floor(k)||(k < 0)
   error('Input argument "k" must be a non-negative integer')
end
if b ~= floor(b)||(b < 2)
   error('Input argument "b" must be a positive integer greater than 1')
end
s = zeros(k+1,1);
for i = 1:k
    a = basexpflip(i,b);
    g = b.^(1:length(a));
    s(i+1) = sum(a./g);
end    

function[a] = basexpflip(k,b) % reversed base-b expansion of positive integer k
j = fix(log(k)/log(b)) + 1;
a = zeros(1,j);
q = b^(j-1);
for i = 1:j
   a(i) = floor(k/q);
   k = k - q*a(i);
   q = q/b;
end
a = fliplr(a);