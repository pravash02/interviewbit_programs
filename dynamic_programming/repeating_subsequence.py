class Solution:

    def solve(self, A):
        n = len(A)
        m = len(A)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == A[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if dp[-1][-1] in [0, 1]:
            return 0
        return 1


if __name__ == '__main__':
    s = Solution()
    A = "abbbbbbcdgf"
    print(s.solve(A))
