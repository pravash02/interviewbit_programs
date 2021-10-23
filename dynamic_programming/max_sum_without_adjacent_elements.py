class Solution:

    def adjacent(self, A):
        t = []
        for i in range(len(A[0]) + 1):
            t.append(-1)
        for i in range(len(A[0]) + 1):
            if i == 0:
                t[i] = 0
            elif i - 2 >= 0:
                u = A[0][i - 1] + t[i - 2]
                v = A[1][i - 1] + t[i - 2]
                w = t[i - 1]
                t[i] = max(u, v, w)
            else:
                u = A[0][i - 1]
                v = A[1][i - 1]
                w = t[i - 1]
                t[i] = max(u, v, w)

        return t[len(A[0])]


if __name__ == '__main__':
    s = Solution()
    A = [[1]
         [2]]
    s.adjacent(A)
