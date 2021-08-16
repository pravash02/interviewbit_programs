class Solution:
    @staticmethod
    def solve(A, B):
        A = list(A)
        A.sort()
        ans = {}
        for i in range(len(A)):
            if A[i] in ans:
                return 1
            else:
                ans[B + A[i]] = i
        return 0

    @staticmethod
    def solveB(A, B):
        n = len(A)
        i = 0
        j = 1
        while (i <= j) and (j < n):
            if i == j:
                j += 1
            elif abs(A[j] - A[i]) == B:
                return 1
            elif abs(A[j] - A[i]) < B:
                j += 1
            elif abs(A[j] - A[i]) > B:
                i += 1
        return 0


if __name__ == '__main__':
    s = Solution
    A = [1, 5, 3]
    B = 2
    print(s.solve(A, B))
    print(s.solveB(A, B))
