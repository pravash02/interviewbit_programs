class Solution:

    @staticmethod
    def smaller_elem(A, B):
        first = 0
        last = len(A)-1
        count = 0
        while first <= last:
            if A[first] <= B:
                count += 1
            else:
                pass

            first += 1

        return count

    @staticmethod
    def smaller_elemB(A, B):
        if B > A[-1]:
            return len(A)
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right) // 2
            if A[mid] < B:
                left = mid + 1
            else:
                right = mid - 1

        while mid <= len(A) - 1 and A[mid] <= B:
            mid = mid + 1

        return mid


if __name__ == '__main__':
    s = Solution
    n = [1, 3, 4, 4, 6]
    n1 = 4
    print(s.smaller_elem(n, n1))
