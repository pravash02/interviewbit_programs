import math


class Solution:
    @staticmethod
    def coprime_div(A, B):
        res = 0
        for i in range(1, A):
            if A % i == 0 and math.gcd(i, B) == 1:
                res = i

        return res


    @staticmethod
    def coprime_divB(A, B):
        while math.gcd(A, B) != 1:
            A = A // math.gcd(A, B)

        return A


    @staticmethod
    def coprime_divC(A, B):
        return A if math.gcd(A, B) == 1 else Solution.coprime_divC(A // math.gcd(A, B), B)


if __name__ == '__main__':
    s = Solution
    a = 30
    b = 12
    print(s.coprime_divB(a, b))
