class Solution:
    @staticmethod
    def solve(A):
        q = 0
        t = 1
        for i in range(1, len(A)):
            if A[i] != A[q]:
                q = t
                A[i], A[t] = A[t], A[i]
                t += 1

        return t


if __name__ == '__main__':
    s = Solution
    A = [1, 1, 1, 2, 2]
    print(s.solve(A))
