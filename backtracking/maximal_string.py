class Solution:
    @staticmethod
    def solve(A, B):
        if len(A) <= 1:
            return A

        ans = Solution.recurse(0, list(A), B)
        return str(ans)

    @staticmethod
    def recurse(idx, A, B):
        n = len(A)
        # base case
        if idx == n - 1 or B == 0:
            a = A.copy()
            return ''.join(a)

        # recursive case
        ans = -float('inf')
        for i in range(idx, n):
            A[i], A[idx] = A[idx], A[i]
            if i != idx:
                B -= 1
            ans = max(int(Solution.recurse(idx + 1, A, B)), ans)
            A[i], A[idx] = A[idx], A[i]
        return ans


if __name__ == '__main__':
    s = Solution
    A = "234"
    print(s.solve(A, 2))
