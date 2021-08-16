class Solution:

    @staticmethod
    def solve(A, B):
        # O(N * Log(N))
        A.sort()
        result = set()

        # O(N ^ 2) Time
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                lo, hi = j + 1, len(A) - 1

                # O(N) Time
                while lo < hi:
                    x = A[i] + A[j] + A[lo] + A[hi]

                    if x == B:
                        result.add((A[i], A[j], A[lo], A[hi]))
                        hi -= 1
                        lo += 1

                    elif x > B:
                        hi -= 1
                    else:
                        lo += 1

        return sorted(result)


if __name__ == '__main__':
    s = Solution
    A = [1, 0, -1, 0, -2, 2]
    B = 0
    print(s.solve(A, B))
