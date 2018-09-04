% k = 100;
nd = 3;
k = 4000;
D1 = [];
D2 = [];
D3 = [];
P = randn(nd,k);
X1k = (P ./ (ones(nd,1) * sqrt(sum(P.^2))))';
X2k = sphere_n(k,nd-1,[2 3 5 7]);
%%X3k = sphere_n(k,nd-1,[2 5 3 7]);

for i=100:100:k
   X1 = X1k(1:i,:);
   K1 = convhulln(X1);
   %%d1 = discrep(K1,X1);
   d1 = discrep_2(K1,X1);
   D1 = [D1, d1];
   
   X2 = X2k(1:i,:);
   K2 = convhulln(X2);
   %%d2 = discrep(K2,X2);
   d2 = discrep_2(K2,X2);
   D2 = [D2, d2];

   %% X3 = X3k(1:i,:);
   %% K3 = convhulln(X3);
   %% d3 = discrep_2(K3,X3);
   %% D3 = [D3, d3];
end
figure
ax = [100:100:k];
plot(ax, D1,'r-');
hold on
plot(ax, D2,'b-');
%% plot(ax, D3,'g-');
legend('random', 'our');
xlabel('#points');
ylabel('discrepancy');
