class Solution:

    def chainPairs(self, A):
        row = len(A)
        col = len(A[0])
        t = []
        dp = [1] * row
        print(dp)
        for i in range(row):
            for j in range(0, i):
                if A[i][0] > A[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print(dp)
        return max(dp)

    def solve(self, A):
        return self.chainPairs(A)


if __name__ == '__main__':
    s = Solution()
    A = [[5, 24],
         [39, 60],
         [15, 28],
         [27, 40],
         [50, 90]]
    print(s.solve(A))
