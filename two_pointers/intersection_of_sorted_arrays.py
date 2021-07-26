class Solution:
    @staticmethod
    def solve(A, B):
        C = []
        strt_A = 0
        strt_B = 0

        while strt_A < len(A) and strt_B < len(B):
            if A[strt_A] == B[strt_B]:
                C.append(A[strt_A])
                strt_B += 1
                strt_A += 1
            elif A[strt_A] > B[strt_B]:
                strt_B += 1
            else:
                strt_A += 1

        return C

    @staticmethod
    def solveB(A, B):
        res = set({})
        for i in A:
            if i in B:
                res.add(i)

        return sorted(list(res))


if __name__ == '__main__':
    s = Solution
    A = [1, 2, 3, 4]
    B = [2, 3, 9]
    print(s.solve(A, B))
    print(s.solveB(A, B))
