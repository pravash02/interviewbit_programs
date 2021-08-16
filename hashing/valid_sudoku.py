class Solution:
    @staticmethod
    def solve(A):
        rows = [set() for _ in range(len(A))]
        cols = [set() for _ in range(len(A))]
        grid = [set() for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(len(A)):
                current = A[i][j]
                if current != '.':
                    size = (i // 3) * 3 + j // 3
                    if current in rows[i] or current in cols[j] or current in grid[size]:
                        return 0
                    rows[i].add(current)
                    cols[j].add(current)
                    grid[size].add(current)
        return 1


if __name__ == '__main__':
    s = Solution
    A = ["53..7....", "6..195...", ".98....6.", "8...6...3",
         "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
    print(s.solve(A))
