def test3():
    k = 500
    nd = 3
    
    X1 = sphere_n(k,nd-1,[2 3])
    K1 = convhulln(X1)
    d1 = discrep(K1,X1)
    disp('low discrepancy...')
    disp(d1)
    subplot(1,2,1),
    trisurf(K1,X1(:,1),X1(:,2),X1(:,3))
    axis('square')
    
    P = randn(nd,k)
    X2 = (P ./ (ones(nd,1) * math.sqrt(sum(P**2))))'
    K2 = convhulln(X2)
    d2 = discrep(K2,X2)
    disp('random sequence...')
    disp(d2)
    subplot(1,2,2),
    trisurf(K2,X2(:,1),X2(:,2),X2(:,3))
    axis('square')