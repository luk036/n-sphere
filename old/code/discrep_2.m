function[dis] = discrep_2(K, X)
% measure discrepancy
% K = convhulln(X);
[nsimplex, n] = size(K);
maxd = 0;
mind = 1000;
for k=1:nsimplex,
  p = X(K(k,:),:)';
  for i=1:n-1,
   	for j=i+1:n,
   	  dot = p(:,i)'*p(:,j);
      d = sqrt(1.0 - dot*dot);
      if (maxd < d), maxd = d; end
      if (mind > d), mind = d; end
    end
  end
end
dis = maxd - mind;
