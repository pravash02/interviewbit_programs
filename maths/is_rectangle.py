class Solution:
    @staticmethod
    def is_rect(A, B, C, D):
        if A == B and C == D:
            return 1
        elif A == C and B == D:
            return 1
        elif A == D and B == C:
            return 1
        else:
            return 0


if __name__ == '__main__':
    s = Solution
    a = 1
    b = 1
    c = 3
    d = 3
    print(s.is_rect(a, b, c, d))
