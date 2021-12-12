from math import sqrt
import random

def FuncPi(x):
    return sqrt(1-x*x)

def HitorMiss(n, f = None):
    k = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if y < f(x):
            k = k + 1
    return k/n

if __name__ == '__main__':
    pi = 3.141593
    lt = [10000, 100000, 1000000, 10000000, 100000000]
    for i in lt:
        result = 4*HitorMiss(i, FuncPi)
        print(result, 'wucha:', abs(pi-result))