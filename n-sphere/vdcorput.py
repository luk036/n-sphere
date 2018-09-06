def vdc(n, base=2):
    vdc, denom = 0.0, 1.0
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder / denom
    return vdc


def vdcorput(n, base=2):
    '''
    n - number of vectors
    base - seeds
    '''
    for i in range(n):
        yield vdc(i, base)


if __name__ == "__main__":
    for s in vdcorput(10, 2):
        print(s)
