class Solution:
    def solve(self, x):
        maxi = 0
        for i in range(len(A)):
            for j in range(i + 1):
                if i == 0 and j == 0:
                    pass
                elif j == 0:
                    A[i][j] += A[i - 1][j]
                else:
                    A[i][j] += max(A[i - 1][j], A[i - 1][j - 1])
                if i == len(A) - 1:
                    maxi = max(maxi, A[i][j])
        return maxi


if __name__ == '__main__':
    s = Solution()
    A = [
        [8, 0, 0, 0],
        [4, 4, 0, 0],
        [2, 2, 6, 0],
        [1, 1, 1, 1]
    ]
    print(s.solve(A))
