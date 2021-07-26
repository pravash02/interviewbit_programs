import math


class Solution:
    @staticmethod
    def power(A):
        x = math.log2(int(A))
        y = int(x)
        if (x == y and y >= 1):
            return 1
        return 0

    @staticmethod
    def powerB(A):
        if A == "1":
            return 0
        b = bin(int(A)).replace("0b", "")
        if (b.count('1') == 1 and b[0] == '1'):
            return 1
        return 0

    @staticmethod
    def powerC(A):
        return 1 if (int(A) & (int(A) - 1) == 0 and int(A) >= 2) else 0


if __name__ == '__main__':
    s = Solution
    M = 128
    print((128 + 127) // 2)
    print(int(M) & (int(M)-1))
    print(s.power(M))
