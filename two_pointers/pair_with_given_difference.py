class Solution:
    @staticmethod
    def solve(A, B):
        if len(A) == 0:
            return 0

        A.sort()
        for i in range(0, len(A)):
            if A[i] - B in A and A[i] != B:
                return 1

        return 0

    @staticmethod
    def solveB(A, B):
        i = 0
        j = 1
        A.sort()
        n = len(A)
        while i < n and j < n:
            if i != j and A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j += 1
            else:
                i += 1
        return 0

    @staticmethod
    def solveC(A, B):
        A.sort()

        for i in range(0, len(A)):
            j = len(A) - 1
            while j > 0:
                if i != j and A[j] - A[i] == B:
                    return 1
                elif A[j] - A[i] < B:
                    break
                else:
                    j -= 1

        return 0


if __name__ == '__main__':
    s = Solution
    M = [1, 4, 5, 6, 7]
    M1 = [10, 20]
    N = 4
    N1 = 10
    print(s.solveC(M1, N1))
