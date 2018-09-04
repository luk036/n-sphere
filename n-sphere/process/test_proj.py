def test_proj():
    k = 400
    nd = 3
    
    X = sphere_n(k,nd,[2 3 5])
    X = X(2:k,:)
    
    X1 = X(:,[1 2 3])'
    # normalize
    X1 = (X1 ./ (ones(nd,1) * math.sqrt(sum(X1**2))))'
    K1 = convhulln(X1)
    #d1 = discrep(K1,X1)
    disp('low discrepancy...')
    #disp(d1)
    subplot(2,2,1),
    trisurf(K1,X1(:,1),X1(:,2),X1(:,3))
    axis('square')
    
    X1 = X(:,[2 3 4])'
    # normalize
    X1 = (X1 ./ (ones(nd,1) * math.sqrt(sum(X1**2))))'
    K1 = convhulln(X1)
    #d1 = discrep(K1,X1)
    disp('low discrepancy...')
    #disp(d1)
    subplot(2,2,2),
    trisurf(K1,X1(:,1),X1(:,2),X1(:,3))
    axis('square')
    
    X1 = X(:,[1 2 4])'
    # normalize
    X1 = (X1 ./ (ones(nd,1) * math.sqrt(sum(X1**2))))'
    K1 = convhulln(X1)
    #d1 = discrep(K1,X1)
    disp('low discrepancy...')
    #disp(d1)
    subplot(2,2,3),
    trisurf(K1,X1(:,1),X1(:,2),X1(:,3))
    axis('square')
    
    X1 = X(:,[1 3 4])'
    # normalize
    X1 = (X1 ./ (ones(nd,1) * math.sqrt(sum(X1**2))))'
    K1 = convhulln(X1)
    #d1 = discrep(K1,X1)
    disp('low discrepancy...')
    #disp(d1)
    subplot(2,2,4),
    trisurf(K1,X1(:,1),X1(:,2),X1(:,3))
    axis('square')
    