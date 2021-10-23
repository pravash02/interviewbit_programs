class Solution:

    def solve(self, A, B):
        A = list(A)
        B = list(B)
        m = len(A)
        n = len(B)
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(m):
            for j in range(n):
                # swap/identical last char
                a = dp[i][j] + (0 if A[i] == B[j] else 1)
                # remove last char
                b = dp[i][j + 1] + 1
                # add last char
                c = dp[i + 1][j] + 1

                dp[i + 1][j + 1] = min(a, b, c)

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    A = "abad"
    B = "abac"
    s.solve(A, B)
