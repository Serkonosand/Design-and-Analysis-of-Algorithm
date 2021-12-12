import random
import math

def setcount(x):
    k = 0
    S = set()
    a = random.randint(1, x)
    while True:
        k+=1
        S.add(a)
        a = random.randint(1, x)
        if a in S:
            break
    return k

def SetCount(x):
    num = 10000
    sum = 0
    for i in range(num):
        sum += setcount(x)
    avg_k = sum/num
    return 2*avg_k**2/math.pi


if __name__ == '__main__':
    for n in range(1,8):
        x = math.pow(10, n)
        print(x, ':', int(SetCount(x)))