import random

def Darts(n):
    k = 0;
    for i in range(n):
        x = random.random()
        y = x
        if x*x + y*y <= 1:
            k = k + 1
    return (4*k/n)

if __name__ == "__main__":
    lt = [10000, 100000, 1000000, 10000000, 100000000]
    for i in lt:
        print(Darts(i))
