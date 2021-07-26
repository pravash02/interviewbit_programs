class Solution:
    @staticmethod
    def solve(A, B):
        s = set()
        for i in A:
            if i + B in s or i - B in s:
                return 1
            else:
                s.add(i)

        return 0

    ### sliding window
    @staticmethod
    def solveB(A, B):
        i = 0
        j = 1
        while j < len(A):
            if i == j:
                j += 1
            else:
                if A[j] - A[i] == B:
                    return 1
                elif A[j] - A[i] < B:
                    j += 1
                else:
                    i += 1
        return 0


if __name__ == '__main__':
    s = Solution
    A = [1, 3, 5]
    B = 4
    print(s.solve(A, B))
    print(s.solveB(A, B))
