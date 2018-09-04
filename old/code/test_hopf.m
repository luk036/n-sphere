clear all;
k = 5000;
n = 4;
D1 = [];
D2 = [];
D3 = [];
P = randn(n,k);
X1k = (P ./ (ones(n,1) * sqrt(sum(P.^2))))';
X2k = sphere3(k,[2 3 5]);
X3k = sphere3_hopf(k,[2 3 5]);

for k=100:100:5000
   X1 = X1k(1:k,:);
   K1 = convhulln(X1);
   %%d1 = discrep(K1,X1);
   d1 = discrep_2(K1,X1);
   D1 = [D1, d1];
   

   X2 = X2k(1:k,:);
   K2 = convhulln(X2);
   %d2 = discrep(K2,X2);
   d2 = discrep_2(K2,X2);
   D2 = [D2, d2];
   
   X3 = X3k(1:k,:);
   K3 = convhulln(X3);
   %%d3 = discrep(K3,X3);
   d3 = discrep_2(K3,X3);
   D3 = [D3, d3];
end
figure
ax = [100:100:5000];
plot(ax, D1,'r-');
hold on
plot(ax, D2,'b-');
plot(ax, D3,'g-');