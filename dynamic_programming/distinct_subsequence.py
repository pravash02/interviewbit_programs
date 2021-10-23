class Solution:
    def numDistinct(self, s, t):
        n = len(s)
        m = len(t)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, n + 1):
            dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(i, n + 1):
                if i == 1 and j == 1:
                    if t[i - 1] == s[j - 1]:
                        dp[i][j] = 1
                else:
                    if t[i - 1] == s[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    A = "abc"
    B = "abc"
    print(s.numDistinct(A, B))
