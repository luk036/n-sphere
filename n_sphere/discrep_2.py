import numpy as np


def discrep_2(K, X):
    """
    measure discrepancy
    K = convhulln(X)
    """
    nsimplex, n = K.shape
    maxd = 0
    mind = 1000
    for k in range(nsimplex):
        p = X[K[k, :], :]
        for i in range(n-1):
            for j in range(i+1, n):
                dot = np.dot(p[i, :], p[j, :])
                d = 1.0 - dot*dot
                if maxd < d:
                    maxd = d
                if mind > d:
                    mind = d
    dis = np.arcsin(np.sqrt(maxd)) - np.arcsin(np.sqrt(mind))
    return dis
