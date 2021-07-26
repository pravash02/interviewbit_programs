class Solution:
    @staticmethod
    def large_fact(A):
        f = 1
        for i in range(2, A + 1):
            f *= i
        return f


if __name__ == '__main__':
    s = Solution
    lst = 3
    print(s.large_fact(lst))
