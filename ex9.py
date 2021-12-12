from random import randint
class Queen(object):
    def __init__(self):
        self.__trycnt = 0

    def queensLV(self, stepVegas, x, n):
        col = set()
        diag45 = set()
        diag135 = set()
        k = 0
        while True:
            nb = 0
            j = 0
            for i in range(n):
                if (i not in col) and (i - k not in diag45) and (i + k not in diag135):
                    nb += 1
                    if randint(1, nb) == 1:
                        j = i
            if nb > 0:
                x[k] = j
                self.__trycnt += 1
                col.add(j)
                diag45.add(j - k)
                diag135.add(j + k)
                k += 1
            if nb == 0 or k == stepVegas:
                if nb > 0:
                    return self.backtrace(k, x, n)
                else:
                    return False


    def test(self, k, x):
        for i in range(0, k):
            if x[i] == x[k] or abs(x[k] - x[i]) == abs(k - i):
                return False
        return True


    def backtrace(self, start, x, n):
        if start >= n:
            return True
        for i in range(0, n):
            x[start] = i
            if self.test(start, x):
                self.__trycnt += 1
                if self.backtrace(start + 1, x, n):
                    return True
        return False

    def search(self, stepV, x, n):
        self.__trycnt = 0
        while 1:
            if self.queensLV(stepV, x, n):
                return self.__trycnt
                


if __name__ == '__main__':
    total = 100
    Qn = Queen()
    # queen numbers
    for n in range(12, 21):
        # stepvegas choice
        print('queen number:',n)
        beststep = 0
        min = 0       
        for stepVegas in range(1, n+1):
            # avg
            sum = 0 
            for _ in range(total):
                x = [-1 for _ in range(n)]
                sum += Qn.search(stepVegas, x, n)
            if beststep == 0 or sum < min:
                min = sum
                beststep = stepVegas
        print('n=',n,'beststep=',beststep,'nodes=',min/total)