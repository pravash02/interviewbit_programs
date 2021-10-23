class Solution:

    def solve(self, A):
        import sys
        sys.setrecursionlimit(10 ** 6)
        B = A[::-1]
        l = len(A)
        t = [[-1] * (l + 1) for i in range(l + 1)]

        def sol(i, j):
            if i == -1 or j == -1:
                return 0
            if t[i][j] != -1:
                return t[i][j]
            if A[i] == B[j]:
                t[i][j] = 1 + sol(i - 1, j - 1)
            else:
                t[i][j] = max(sol(i - 1, j), sol(i, j - 1))
            return t[i][j]

        return sol(l - 1, l - 1)


if __name__ == '__main__':
    s = Solution()
    A = "abbcdgf"
    print(s.solve(A))
