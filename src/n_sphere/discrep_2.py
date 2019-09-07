import numpy as np


def discrep_2(K, X):
    """dispersion measure

    Arguments:
        K {[type]} -- [description]
        X {[type]} -- [description]

    Returns:
        float -- dispersion
    """
    nsimplex, n = K.shape
    maxq = 0
    minq = 1000
    for k in range(nsimplex):
        p = X[K[k, :], :]
        for i in range(n - 1):
            for j in range(i + 1, n):
                dot = np.dot(p[i, :], p[j, :])
                q = 1.0 - dot * dot
                if maxq < q:
                    maxq = q
                if minq > q:
                    minq = q
    dis = np.arcsin(np.sqrt(maxq)) - np.arcsin(np.sqrt(minq))
    return dis
