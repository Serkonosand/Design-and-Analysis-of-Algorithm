
import random
from math import sqrt

class Sherwood(object):
    # initialize random list
    def __init__(self):
        self.__N = 10000
        self.__cnt = 0
        self.__val = []
        self.__ptr = []
        self.__head = 0
        for i in range(self.__N):
            self.__val.append(i)
        random.shuffle(self.__val)
        for i in self.__val:
            if i == self.__N - 1:
                self.__ptr.append(0)
            else:
                self.__ptr.append(self.__val.index(i+1))
        self.__head = self.__val.index(0)

    # search function
    def search(self, x, i):
        while x > self.__val[i]:
            i = self.__ptr[i]
            self.__cnt+=1
        return i, self.__cnt
    
    # cnt = 0
    def cnt_zero(self):
        self.__cnt = 0

    # return x
    def val_x(self):
        return random.randint(0, self.__N)

    def alg_a(self,x):
        self.cnt_zero()
        return self.search(x, self.__head)

    def alg_b(self,x):
        self.cnt_zero()
        ind = self.__head
        maxn = ind
        for j in range(int(sqrt(self.__N))):
            self.__cnt+=1
            if self.__val[maxn] < self.__val[j] and self.__val[j] <= x:
                maxn = j
        return self.search(x, maxn)

    def alg_c(self,x):
        self.cnt_zero()
        ind = self.__head
        maxn = ind
        for j in range(int(sqrt(self.__N))):
            self.__cnt+=1
            randj = random.randint(0, self.__N-1)
            if self.__val[maxn] < self.__val[randj] and self.__val[randj] <= x:
                maxn = randj
        return self.search(x, maxn)

    def alg_d(self,x):
        self.cnt_zero()
        ind = random.randint(0, self.__N)
        y = self.__val[ind]
        self.__cnt += 1
        if x < y:
            return self.search(x, self.__head)
        elif x > y:
            return self.search(x, self.__ptr[ind])
        else:
            return ind, self.__cnt


if __name__ == '__main__':
    S = Sherwood()
    sa = []
    sb = []
    sc = []
    sd = []
    for i in range(1000):
        x = S.val_x()
        sa.append(S.alg_a(x)[1])
        sb.append(S.alg_b(x)[1])
        sc.append(S.alg_c(x)[1])
        sd.append(S.alg_d(x)[1])
    print('algA:',sum(sa) / len(sa), max(sa))
    print('algB:',sum(sb) / len(sb), max(sb))
    print('algC:',sum(sc) / len(sc), max(sc))
    print('algD:', sum(sd) / len(sd), max(sd))