import math


class Solution:
    @staticmethod
    def findMedianSortedArrays(A, B):
        if len(A) > len(B):
            return Solution.findMedianSortedArrays(B, A)

        start_a = 0
        end_a = len(A)

        start_b = 0
        end_b = len(B)

        while (start_a <= end_a):
            position_a = (start_a + end_a) // 2
            position_b = (len(A) + len(B) + 1) // 2 - position_a    # +1 for even and odd

            max_left_a = float('-inf') if position_a == 0 else A[position_a - 1]
            min_right_a = float('inf') if position_a == len(A) else A[position_a]

            max_left_b = float('-inf') if position_b == 0 else B[position_b - 1]
            min_right_b = float('inf') if position_b == len(B) else B[position_b]

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (len(A) + len(B)) % 2 == 0:
                    return math.avg(max(max_left_a, max_left_b) + min(min_right_a, min_right_b))
                else:
                    return max(max_left_a, max_left_b)

            elif max_left_a > min_right_b:
                end_a = position_a - 1
            else:
                start_a = position_a + 1

    ### below code not working
    @staticmethod
    def findMedianSortedArraysB(A, B):
        m = len(A)
        n = len(B)

        if m > n:
            A, B, m, n = B, A, n, m

        imin = 0
        imax = m
        half_len = (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    s = Solution
    x = [1, 3, 5, 8, 9]
    y = [7, 8, 11, 14, 16, 18]
    print(s.findMedianSortedArrays(x, y))
