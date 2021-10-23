class Solution:

    def solve(self, A, B):
        matrix = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if (A[i - 1] == B[j - 1]):
                    # diagonal val + 1
                    matrix[j][i] = matrix[j - 1][i - 1] + 1
                else:
                    # max of diagonals
                    matrix[j][i] = max(matrix[j - 1][i], matrix[j][i - 1])
        # print(matrix)
        return matrix[len(B)][len(A)]


if __name__ == '__main__':
    s = Solution()
    A = "abbcdgf"
    B = "bbadcgf"
    print(s.solve(A, B))
