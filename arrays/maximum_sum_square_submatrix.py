import sys


class Solution:
    @staticmethod
    def max_submatrix_sum(A, B):
        max_sum = float('-inf')
        row_length = len(A)
        col_length = len(A[0])

        for i in range(0, row_length):
            for j in range(0, col_length):

                if i + B <= row_length and j + B <= col_length:
                    summ = 0
                    for k in range(i, i + B):
                        for l in range(j, j + B):
                            summ += A[k][l]

                    max_sum = max(summ, max_sum)

        return max_sum

    ### Dynamic Programming
    @staticmethod
    def max_submatrix_sumB(A, B):
        max_sum = -float('inf')
        row_length = len(A)
        col_length = len(A[0])

        ###
        dup_lst = [[0 for x in range(col_length + 1)] for y in range(row_length + 1)]
        dup_lst[0][0] = A[0][0]

        for i in range(1, row_length + 1):
            for j in range(1, col_length + 1):
                dup_lst[i][j] = A[i - 1][j - 1] + dup_lst[i - 1][j] + dup_lst[i][j - 1] - dup_lst[i - 1][j - 1]

        for i in range(1, row_length + 1):
            for j in range(1, col_length + 1):
                summ = dup_lst[i][j]
                if i - B <= row_length + 1 and j - B <= col_length + 1:
                    summ = dup_lst[i][j] - dup_lst[i - B][j] - dup_lst[i][j - B] + dup_lst[i - B][j - B]
                    max_sum = max(max_sum, summ)
                    p = (i, j)

        return max_sum

    ### Dynamic Programming 2
    @staticmethod
    def max_submatrix_sumC(A, B):
        n = len(A)
        m = len(A[0])
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # for i in range(1, n + 1):
        #     dp[i][1] = dp[i - 1][0] + A[i - 1][0]
        # for j in range(1, m + 1):
        #     dp[1][j] = dp[0][j - 1] + A[0][j - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = A[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        ans = -float("inf")
        for i in range(1, n + 1):
            if i + B - 1 < n + 1:
                for j in range(1, m + 1):
                    if j + B - 1 > m:
                        break
                    t = dp[i + B - 1][j + B - 1] - dp[i - 1][j + B - 1] - dp[i + B - 1][j - 1] + dp[i - 1][j - 1]
                    ans = max(ans, t)
        return ans


if __name__ == '__main__':
    s = Solution
    lst = [[1, 0, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    B = 3
    print(s.max_submatrix_sumB(lst, B))
    print(s.max_submatrix_sumC(lst, B))
