class Solution:
    @staticmethod
    def perfect_peakA(A):
        max_left = A[0]
        min_right = cur_min_right = A[len(A)-1]
        d = {}
        d['left_elem'] = 0

        for i in range(1, len(A)-1):
            max_left = max(A[d['left_elem']:i])
            min_right = min(A[i+1:])

            if A[i] > A[d['left_elem']]:
                d['left_elem'] = i
            if max_left < A[i] < min_right:
                return 1

        return 0

    @staticmethod
    def perfect_peakB(A):
        left_max = A[0]
        right_max = A[0]
        ans = 0
        n = len(A)

        for i in range(1, n):
            if A[i] > right_max:
                right_max = A[i]
            if A[i] > left_max:
                if ans == 0:
                    left_max = right_max
                ans = 1
            if A[i] < left_max:
                ans = 0
                left_max = right_max
        if left_max == A[n - 1]:
            return 0
        return ans


if __name__ == '__main__':
    s = Solution
    lst = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    lst2 = [5, 1, 4, 3]
    lst3 = [10549, 15882, 24856, 301, 16642, 14414, 19856]
    print(s.perfect_peakA(lst))
    # print(s.perfect_peakB(lst))
