import math


class Solution:
    @staticmethod
    def check_prime(n):
        if n == 1:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def prime_sum(A):
        for i in range(1, A // 2 + 1):
            if Solution.check_prime(i) and Solution.check_prime(A - i):
                return [i, A - i]


    @staticmethod
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def prime_sumB(A):
        lst = []
        for i in range(2, A):
            if Solution.is_prime(i):
                lst.append(i)

        for i in lst:
            if A-i in lst:
                return [i, A-i]


if __name__ == '__main__':
    s = Solution
    lst = 7
    print(s.prime_sumB(lst))
