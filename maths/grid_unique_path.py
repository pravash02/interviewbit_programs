class Solution:

    ### Using maths Combination method: ex-nCm with n = col_length, m = row steps
    @staticmethod
    def grid_unique_path(A, B):
        N = A + B - 2   ### total directions possible
        d = A - 1       ### number of downward steps possible
        res = 1
        i = 1
        while i <= d:
            res = res * (N - d + i) // i
            i += 1

        return res

    @staticmethod
    def grid_unique_pathB(A, B):
        if A == 1:
            return 1
        Ans = [1] * B
        for i in range(1, A):
            for j in range(1, B):
                Ans[j] += Ans[j - 1]
        return Ans[-1]


if __name__ == '__main__':
    s = Solution
    a = 2
    b = 3
    print(s.grid_unique_path(a, b))
