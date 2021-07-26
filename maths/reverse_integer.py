class Solution:

    @staticmethod
    def reverse_int(A):
        B = abs(A)
        lst_int = list(str(B))
        rev_int = "".join(i for i in lst_int[::-1])
        c = int(rev_int)
        if c > 2 ** 31:
            return 0
        else:
            if A >= 0:
                return c
            else:
                return -c


if __name__ == '__main__':
    s = Solution
    n = 101
    print(s.reverse_int(n))
