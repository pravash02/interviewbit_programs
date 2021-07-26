import math


class Solution:
    @staticmethod
    def is_power(A):
        if A == 1:
            return 1
        res = False
        i = 2
        while i * i <= A:
            if (abs(math.log(A, i) - int(math.log(A, i))) < 0.000001):
                res = True
            i += 1

        return int(res)

    @staticmethod
    def is_powerB(A):
        if A == 1:
            return 1

        for i in range(2, int(math.sqrt(A) + 1)):
            p = math.log(A, i)
            p = float("{0:.5f}".format(p))
            if p % 2 == 0 or (p + 1) % 2 == 0:
                return 1
        return 0

    @staticmethod
    def is_powerC(n):
        if n == 1:
            return 1
        res = False
        for i in range(2, int(math.sqrt(n)+1)):
            p = math.log(n, i)
            if math.pow(i, p) == n:
                res = True
                return int(res)

        return int(res)


if __name__ == '__main__':
    s = Solution
    n = 4
    # print(int(math.sqrt(4)+1))
    # print(math.log(4, 2))
    # print(math.pow(2, math.log(4, 2)))
    # print(s.is_power(n))
    print(s.is_powerB(n))
    print(s.is_powerC(n))
