class Solution:
    @staticmethod
    def gcd(A, B):
        if A < B:
            A, B = B, A

        while B:
            A, B = B, A % B

        return A

    @staticmethod
    def gcd2(m, n):
        while m != 0:
            r = n % m
            n = m
            m = r

        return n


if __name__ == '__main__':
    s = Solution
    a = 6
    b = 2
    s.gcd(a, b)
    print(s.gcd2(a, b))
