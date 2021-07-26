class Solution:
    @staticmethod
    def divide_int(A, B):
        if A == 0:
            return 0
        isNegative = (A < 0) ^ (B < 0)
        A = abs(A)
        B = abs(B)

        multiples = 1
        while A >= (B << 1):
            B <<= 1
            multiples <<= 1
        result = 0
        while multiples >= 1:
            if A >= B:
                A -= B
                result += multiples
            multiples >>= 1
            B >>= 1
        if isNegative:
            return -result if -result > -2 ** 31 else -2 ** 31
        else:
            return result if result < 2 ** 31 - 1 else 2 ** 31 - 1


    @staticmethod
    def divide_intB(A):
        pass


if __name__ == '__main__':
    s = Solution
    a = 10
    b = 3
    print(bin(1), (bin(1 << 1)))
    print(bin(6), bin(6 << 1))
    print(s.divide_int(a, b))
