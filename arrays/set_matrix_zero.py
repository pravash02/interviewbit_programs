import copy


class Solution:
    @staticmethod
    def set_matrix(A):
        i = 0
        row_size = len(A)
        col_size = len(A[0])

        row_has_zero = False
        col_has_zero = False

        for col in range(0, col_size):
            if A[0][col] == 0:
                row_has_zero = True

        for row in range(0, col_size):
            if A[row][0] == 0:
                col_has_zero = True

        ##
        for row in range(0, row_size):
            for col in range(0, col_size):
                if A[row][col] == 0:
                    A[row][0] = 0
                    A[0][col] = 0

        ##
        for row in range(1, row_size):
            for col in range(1, col_size):
                if A[row][0] == 0 or A[0][col] == 0:
                    A[row][col] = 0

        if row_has_zero:
            for col in range(0, col_size):
                A[0][col] = 0

        if col_has_zero:
            for row in range(0, row_size):
                A[row][0] = 0

        return A


if __name__ == '__main__':
    s = Solution
    lst = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    print(s.set_matrix(lst))
