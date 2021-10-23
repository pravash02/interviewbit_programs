class Solution:

    def climbStairs(self, A):
        dp = [0] * (A + 1)
        print(dp)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, A + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[A]


if __name__ == '__main__':
    s = Solution()
    A = 2
    print(s.climbStairs(A))
