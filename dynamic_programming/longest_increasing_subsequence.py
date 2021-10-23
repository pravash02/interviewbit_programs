class Solution:

    def solve(self, A):
        n = len(A)
        res = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if A[i] > A[j] and res[i] < res[j] + 1:
                    res[i] = res[j] + 1
        print(res)
        return max(res)


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 1, 5]
    print(s.solve(A))
