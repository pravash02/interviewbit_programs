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
                    size = (i // 3) * 3 + (j // 3)
                    if current in rows[i] or current in cols[i] or current in grid[size]:
                        return 0

                    rows[i].add(i)
                    cols[j].add(j)
                    grid[size].add(current)

        return 1

    ### interviewbit solution
    def solveSudoku(self, A):
        board = A
        flag = False

        for i in range(9):
            for j in range(9):
                tried_all_value = 9
                if board[i][j] == '.':
                    for val in map(str, range(1, 10)):
                        if self.checkConstraint(board, val, i, j):
                            board[i][j] = val
                            self.solveSudoku(board)
                            if board:
                                flag = True
                                for row in board:
                                    if '.' in row:
                                        flag = False
                                        break
                        if flag:
                            break
                        else:
                            board[i][j] = '.'
                        tried_all_value -= 1
                if tried_all_value == 0:
                    return

                if flag: break

            if tried_all_value == 0:
                break
            if flag:
                break

    def checkConstraint(self, board, val, i, j):
        if val in board[i]:
            return False

        for row in board:
            if row[j] == val:
                return False

        for m in range(3):
            for n in range(3):
                if board[(i // 3) * 3 + m][(j // 3) * 3 + n] == val:
                    return False

        return True


if __name__ == '__main__':
    s = Solution
    A = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    print(s.solve(A))
