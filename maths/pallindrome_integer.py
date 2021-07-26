class Solution:
    @staticmethod
    def pallindrome(n):
        lst_int = list(str(n))
        rev_int = "".join(i for i in lst_int[::-1])

        if n == int(rev_int):
            return True

        return False

    @staticmethod
    def pallindromeB(n):
        s = 0
        n_bkp = n

        while n > 0:
            remainder = n % 10
            s = s * 10 + remainder
            n = n // 10

        print(s)
        if s == n_bkp:
            return True

        return False

    @staticmethod
    def pallindromeC(n):
        A = str(n)
        for i in range(len(A) // 2):
            if A[i] == A[len(A) - 1 - i]:
                continue
            return 0
        return 1


if __name__ == '__main__':
    s = Solution
    n = 101
    print(s.pallindromeB(n))
