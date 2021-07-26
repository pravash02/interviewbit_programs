class Solution:
    @staticmethod
    def solve(A, B):
        A = sorted(A)
        n = len(A)
        mindiff = float('inf')

        for i in range(len(A) - 2):
            j = i + 1
            k = n - 1
            while j < k:
                s = A[i] + A[k] + A[j]
                diff = abs(B - s)

                if diff == 0:
                    return s

                if diff < mindiff:
                    mindiff = diff
                    result = s

                if s <= B:
                    j += 1
                else:
                    k -= 1

        return result

    @staticmethod
    def solveB(A, B):
        ans = A[0] + A[1] + A[2]
        A.sort()

        for i in range(len(A) - 2):
            l, r = i + 1, len(A) - 1
            while l < r:
                if abs(ans - B) > abs(A[i] + A[l] + A[r] - B):
                    ans = A[i] + A[l] + A[r]
                if A[i] + A[l] + A[r] > B:
                    r -= 1
                elif A[i] + A[l] + A[r] < B:
                    l += 1
                else:
                    return B
        return ans


if __name__ == '__main__':
    s = Solution
    A = [2, 3, 1, 5, 7, 9]
    B = 3
    print(s.solve(A, B))
    print(s.solveB(A, B))


