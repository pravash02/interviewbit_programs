class Solution:
    def solve(self, A):
        n = len(A)
        if n == 0:
            return 0

        for i in range(1, n):
            A[i][0] += min(A[i - 1][1], A[i - 1][2])
            A[i][1] += min(A[i - 1][0], A[i - 1][2])
            A[i][2] += min(A[i - 1][0], A[i - 1][1])
        return min(A[-1])


if __name__ == '__main__':
    s = Solution()
    A = [
        [1, 2, 3],
        [10, 11, 12]
        ]
    print(s.solve(A))
