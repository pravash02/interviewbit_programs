class Solution:
    @staticmethod
    def solve(A):
        if A == 1:
            return [0, 1]
        else:
            ans = Solution.solve(A - 1)
        return ans + [x + 2 ** (A - 1) for x in ans[::-1]]


if __name__ == '__main__':
    s = Solution
    A = 2
    print(s.solve(A))
