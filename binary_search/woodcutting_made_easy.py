class Solution:
    @staticmethod
    def woodcutting_sum(mid, A):
        s = 0
        for i in range(0, len(A)):
            if A[i] > mid:
                s += (A[i] - mid)
        return s

    @staticmethod
    def woodcutting(A, B):
        left = 0
        right = max(A)
        s = 0

        while left < right:
            mid = (left + right) // 2
            s = Solution.woodcutting_sum(mid, A)
            if s == B or left == mid:
                return mid
            elif s < B:
                right = mid
            else:
                left = mid

        return mid


if __name__ == '__main__':
    s = Solution
    A = [3, 9, 10, 20, 17, 5, 1]
    B = 15
    print(s.woodcutting(A, B))
