class Solution:
    @staticmethod
    def solve(A):
        start = 0
        end = len(A)-1
        for i in range(0, len(A)-1):
            if A[i] == 0:
                A[start], A[i] = A[i], A[start]
                start += 1
            elif A[i] == 2:
                A[end], A[i] = A[i], A[end]
                end -= 1
            else:
                pass

        return A

    @staticmethod
    def solveB(A):
        count0 = count1 = count2 = 0

        for i in range(0, len(A)):
            if A[i] == 0:
                count0 += 1
            elif A[i] == 1:
                count1 += 1
            elif A[i] == 2:
                count2 += 1

        i = 0
        while count0 > 0:
            A[i] = 0
            i += 1
            count0 -= 1
        while count1 > 0:
            A[i] = 1
            i += 1
            count1 -= 1
        while count2 > 0:
            A[i] = 2
            i += 1
            count2 -= 1

        return A


if __name__ == '__main__':
    s = Solution
    M = [1, 0, 2, 0, 0]
    print(s.solve(M))
    print(s.solveB(M))
