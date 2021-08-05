class Solution:
    @staticmethod
    def solve(A):
        max_left = [A[0]]
        max_right = [A[len(A)-1]]
        sum_water = []

        for i in range(1, len(A)):
            max_left.append(max(max_left[i-1], A[i]))

        for i in range(len(A)-2, -1, -1):
            max_right.append(max(max_right[-1], A[i]))

        max_right = max_right[::-1]
        for i in range(len(A)):
            sum_water.append(min(max_right[i], max_left[i]) - A[i])

        return sum(sum_water)


if __name__ == '__main__':
    s = Solution
    A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.solve(A))
