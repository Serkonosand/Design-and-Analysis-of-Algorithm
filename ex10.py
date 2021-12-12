from math import sqrt, log10
from random import randint, random 

class Millrab(object):
    def __init__(self):
        self.__mr_prime = set()
        self.__prime = set()
    
    def btest(self, a, n):
        s = 0
        t = n - 1
        while t % 2 == 0:
            s = s + 1
            t = t // 2
        x = a ** t % n
        if x == 1 or x == n - 1:
            return True
        for i in range(1, s):
            x = x ** 2 % n
            if x == n - 1:
                return True
        return False

    def millrab(self,n):
        a = randint(2, n-2)
        return self.btest(a, n)

    def repeatmillrab(self, n, k):
        for _ in range(1, k+1):
            if self.millrab(n) == False:
                return False
        return True

    def mrgetprime(self):
        self.__mr_prime.clear()
        n = 5
        while True:
            k = int(log10(n))
            if 10000 >= n >= 100 and self.repeatmillrab(n, k):
                self.__mr_prime.add(n)
            n += 2
            if n > 10000:
                break
    
    def getprime(self):
        self.__prime.clear()
        for i in range(100, 10001):
            prime = True
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                self.__prime.add(i)

    def printset(self):
        return self.__mr_prime, self.__prime


if __name__ == '__main__':
    Mr = Millrab()
    Mr.getprime()
    Mr.mrgetprime()
    s1 = Mr.printset()[0]
    s2 = Mr.printset()[1]
    print("total prime numbers:", len(s2))
    print("Millrab result:", len(s1)) 
#    print(":", len(s2.union(s1).difference(s2)))
#    print("少了的素数个数:", len(s2.union(s1).difference(s1)))
    print("accuracy:", len(s1.intersection(s2))/len(s1))
    print(s1)
    print(s2)