class Solution:
    @staticmethod
    def books(A, S):
        def isPossible(mid, A ,S):
            curr_sum = 0
            students = 1
            for i in A:
                if i > mid:
                    return False
                if curr_sum + i > mid:
                    students += 1
                    curr_sum = i
                    if students > S:
                        return False
                else:
                    curr_sum += i
            return True

        if len(A) < S:
            return -1

        total_pages = 0
        for i in A:
            total_pages += i

        start = 0
        end = total_pages
        result = float('inf')
        while start <= end:
            mid = (start + end) // 2

            if isPossible(mid, A, S):
                result = min(result, mid)
                end = mid - 1
            else:
                start = mid + 1
        return result


if __name__ == '__main__':
    s = Solution
    M = [12, 34, 67, 90]
    N = 2
    print(s.books(M, N))
