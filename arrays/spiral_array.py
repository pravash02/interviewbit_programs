class Solution:
    @staticmethod
    def spiral_order(A):
        q = []
        row = 0
        n = len(A) - 1
        col = 0
        m = len(A[0]) - 1
        dir = 0
        while (row <= n and col <= m):
            if (dir == 0):
                for i in range(col, m + 1):
                    q.append(A[row][i])
                row += 1
            elif (dir == 1):
                for i in range(row, n + 1):
                    q.append(A[i][m])
                m -= 1
            elif (dir == 2):
                for i in range(m, col - 1, -1):
                    q.append(A[n][i])
                n -= 1
            elif (dir == 3):
                for i in range(n, row - 1, -1):
                    q.append(A[i][col])
                col += 1
            dir = (dir + 1) % 4
        return q


if __name__ == '__main__':
    print(1%4)
    s = Solution
    lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(s.spiral_order(lst))
