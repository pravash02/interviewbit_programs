from collections import Counter

class Solution:
    @staticmethod
    def solve(A):
        d = Counter(A)
        print(Counter(A).values())
        f = 0
        for v in Counter(A).values():
            if v % 2 == 1 and f == 1:
                return 0
            elif v % 2:     # 1 for true
                f = 1
        return 1


if __name__ == '__main__':
    s = Solution
    A = '232'
    print(s.solve(A))
