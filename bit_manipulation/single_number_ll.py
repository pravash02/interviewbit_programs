class Solution:
    @staticmethod
    def single_num(A):
        if len(A) == 1:
            return A[0]
        A = sorted(A)
        i = 0
        while (i < len(A) - 2):
            if A[i] == A[i + 1]:
                i = i + 3
            else:
                return A[i]

        return A[-1]


if __name__ == '__main__':
    s = Solution
    a = [4, 2, 1, 2, 1, 1, 2]
    print(s.single_num(a))
