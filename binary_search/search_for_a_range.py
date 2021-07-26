class Solution:
    @staticmethod
    def search_range(A, B):
        low = 0
        high = len(A) - 1  # 5

        begin, end = -1, -1

        while low <= high:
            mid = (low + high) // 2
            if A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            else:
                begin = mid
                high = mid - 1

        if begin == -1:
            return [-1, -1]

        low = 0
        high = len(A) - 1  # 5
        while low <= high:
            mid = (low + high) // 2
            if A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            else:
                end = mid
                low = mid + 1

        return [begin, end]


if __name__ == '__main__':
    s = Solution
    A = [5, 7, 7, 8, 8, 10]
    B = 8
    print(s.search_range(A, B))
