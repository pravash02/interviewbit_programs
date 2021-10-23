import math


class Solution:
    def solve(self, A):
        if len(A) <= 1:
            return 0

        answer = -math.inf
        maximum = -math.inf

        for i in range(len(A) - 1, 0, -1):
            if A[i] > maximum:
                maximum = A[i]
            if (maximum - A[i - 1]) > answer:
                answer = (maximum - A[i - 1])

        if answer <= 0:
            return 0

        return answer


if __name__ == '__main__':
    s = Solution()
    A = [1, 4, 5, 2, 4]
    print(s.solve(A))
