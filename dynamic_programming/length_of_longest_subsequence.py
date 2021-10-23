class Solution:

    def solve(self, A):
        n = len(A)
        dp = [1] * n

        for i in range(1, n):
            for j in range(0, i):
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp

    def longest_seq(self, A):
        lis = self.solve(A)
        A = A[::-1]
        lds = self.solve(A)
        lds = lds[::-1]

        result = 0

        for i in range(len(A)):
            result = max(result, lis[i] + lds[i] - 1)

        return result


if __name__ == '__main__':
    s = Solution()
    A = [1, 5, 9]
    print(s.longest_seq(A))
