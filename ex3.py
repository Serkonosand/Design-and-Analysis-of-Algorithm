import math
import random

def FuncSqrt(x):
    return math.sqrt(x)


def sum(a, b, c, d, n, funcptr):
    k = 0
    size = (b-a)*(d-c)
    rect = c*(b-a)
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        if y <= (funcptr(x)):
            k+=1
    return (k/n)*size+rect
        
        
if __name__ == '__main__':
    lt = [10000, 100000, 1000000, 10000000]
    for i in lt:
        print(i, ':', sum(0, 4.0, 0, 2.0, i, FuncSqrt))