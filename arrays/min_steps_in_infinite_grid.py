class Solution:

    @ staticmethod
    def cover_points(A, B):
        tot = 0

        if len(A) == len(B):
            for i in range(len(A) - 1):
                diff_1 = abs(A[i] - A[i + 1])
                diff_2 = abs(B[i] - B[i + 1])

                tot += max(diff_1, diff_2)

        return tot


if __name__ == '__main__':
    s = Solution
    lst = [[-7, -13], [1, -5]]
    for i in range(len(lst)-1):
        print(s.cover_points(lst[i], lst[i+1]))
