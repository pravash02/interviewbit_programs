class Solution:

    @staticmethod
    def max_sub_array(A):
        for i in range(1, len(A)):
            if A[i - 1] > 0:
                A[i] += A[i - 1]
        return max(A)


if __name__ == '__main__':
    s = Solution
    lst = [-163, -5]
    print(s.max_sub_array(lst))
