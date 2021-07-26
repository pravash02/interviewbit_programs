class Solution:
    @staticmethod
    def pascal_tri(A):
        res = []
        for i in range(0, A):
            temp = [int(i) for i in list(str(11**i))]
            res.append(temp)

        return res

    @staticmethod
    def pascal_triB(A):
        pascals_triangle = []

        for i in range(A):
            pascals_triangle.append([1] * (i + 1))

        for i in range(2, A):
            for j in range(1, i):
                pascals_triangle[i][j] = pascals_triangle[i - 1][j - 1] + pascals_triangle[i - 1][j]

        return pascals_triangle


if __name__ == '__main__':
    s = Solution
    a = 5
    print(s.pascal_triB(a))
