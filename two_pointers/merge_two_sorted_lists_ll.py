class Solution:
    ### below function didn't handled the negative cases
    @staticmethod
    def solve(A, B):
        new_lst = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                new_lst.append(A[i])
                i += 1
            else:
                new_lst.append(B[j])
                j += 1

        if i == len(A):
            return new_lst + B[j:]
        else:
            return new_lst + A[i:]

    ### Two Pointers
    @staticmethod
    def solveB(A, B):
        p1 = 0
        p2 = 0

        while p1 < len(A) and p2 < len(B):
            if A[p1] >= B[p2]:
                A.insert(p1, B[p2])
                p1 += 1
                p2 += 1

            elif A[p1] < B[p2]:
                p1 += 1

        if p1 >= len(A) and p2 < len(B):
            A.extend(B[p2:])

        return A

    # @staticmethod
    # def solveC(A, B):
    #     A[:] = sorted(A + B)
    #     # A[:]=[str(i) for i in A]
    #     return A


if __name__ == '__main__':
    s = Solution
    A = [5, 7, 9]
    B = [1, 2, 3, 4]
    print(s.solve(A, B))
    print(s.solveB(A, B))
    # print(s.solveC(A, B))
