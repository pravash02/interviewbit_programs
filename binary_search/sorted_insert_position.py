class Solution:
    @staticmethod
    def insert_pos(A, B):
        first = 0
        last = len(A)

        while first < last:
            mid = (first + last) // 2

            if B < A[mid]:
                last = mid
            elif B == A[mid]:
                return mid
            else:
                first = mid + 1

        return first

    @staticmethod
    def insert_posB(A, B):
        lo, hi = 0, len(A)
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    s = Solution
    n = [1, 3, 4, 6]
    n1 = 4
    print(s.insert_pos(n, n1))
