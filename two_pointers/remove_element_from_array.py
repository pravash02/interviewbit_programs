class Solution:
    @staticmethod
    def solve(A, B):
        n = len(A) - 1
        i = 0
        while i < n:
            if A[i] == B:
                A.remove(A[i])
                i -= 1
                n -= 1
            i += 1

        return len(A)

    ### only for returning the remaining element count
    @staticmethod
    def solveB(A, B):
        count = 0
        for i in range(0, len(A)-1):
            if A[i] == B:
                count += 1

        return len(A) - count

    @staticmethod
    def solveC(A, B):
        ### A[:] creates a shallow copy without extra space
        A[:] = [x for x in A if x != B]
        return len(A)

    ## below code is with extra space
    @staticmethod
    def solveD(A, B):
        C = []
        for i in A:
            if i != B:
                C.append(i)

        return len(C)


if __name__ == '__main__':
    s = Solution
    M = [1, 2, 4, 5, 4, 4, 5]
    N = 4
    print(s.solve(M, N))
    print(s.solveB(M, N))
    print(s.solveC(M, N))
    print(s.solveD(M, N))
