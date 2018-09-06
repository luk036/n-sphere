import numpy as np

def test():
    for i in range(10):
        yield i

def rtest():
    b = test()
    for j in range(10):
        s = [j, next(b)]
        yield s

if __name__ == "__main__":
    for s in rtest():
        print(s)
