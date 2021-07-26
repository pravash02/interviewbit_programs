class Solution:
    @staticmethod
    def solve(A):
        n = len(A)
        to_update = 0
        show_nd = False
        for i in range(1, n):
            if A[i] == A[to_update] and show_nd == False:
                A[to_update + 1] = A[i]
                show_nd = True
                to_update += 1
            elif A[i] == A[to_update] and show_nd == True:
                continue
            else:
                A[to_update + 1] = A[i]
                to_update += 1
                show_nd = False
        A = A[:to_update + 1]
        return len(A)


if __name__ == '__main__':
    s = Solution
    A = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(s.solve(A))
