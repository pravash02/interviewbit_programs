class Solution:
    @staticmethod
    def rotate_matrixA(A):

        print(list(zip(*A[::-1])))

    @staticmethod
    def rotate_matrixB(A):
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        for i in range(len(A)):
            A[i] = reversed(A[i])

        return A


if __name__ == '__main__':
    s = Solution
    lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    lst2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.rotate_matrixA(lst2))
    print(s.rotate_matrixB(lst2))
