class Solution:
    @staticmethod
    def solve(A):
        for i in range(0, len(A)):
            if A.index(A[i]) < i:
                A[A.index(A[i])] += 1
        return A


if __name__ == '__main__':
    s = Solution
    A = [1, 1, 2, 3]
    print(s.solve(A))
