class Solution:
    @staticmethod
    def solve(N):
        col_num = set({})
        pos_diagonal = set({})      # (row + col)
        neg_diagonal = set({})      # (row - col)

        res = []
        board = [["."] * N for i in range(N)]

        def backtrack(row):
            # base case, traveled all rows
            if row == N:
                cp_board = ["".join(each_row) for each_row in board]
                res.append(cp_board)
                return

            for col in range(N):
                if col in col_num or (row+col) in pos_diagonal or (row-col) in neg_diagonal:
                    continue

                col_num.add(col)
                pos_diagonal.add(row+col)
                neg_diagonal.add(row-col)
                board[row][col] = "Q"

                backtrack(row+1)

                col_num.remove(col)
                pos_diagonal.remove(row + col)
                neg_diagonal.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return res


if __name__ == '__main__':
    s = Solution
    A = 4
    print(s.solve(A))
