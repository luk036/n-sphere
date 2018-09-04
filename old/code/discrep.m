function[maxd] = discrep(K,X)
% measure discrepancy (obsoleted)
[k, n] = size(K);
maxd = 0;
mind = 100000;
for i=1:k
   P = X(K(i,:),:);
   d = abs(det(P));
   if (maxd < d), maxd = d; end
   if (mind > d), mind = d; end
end
dis = maxd - mind;