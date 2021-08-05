class Solution:
    @staticmethod
    def solve(A):
        res = []
        A.sort()

        def f(A, subset, index):
            res.append(subset[:])
            for i in range(index, len(A)):
                subset.append(A[i])
                f(A, subset, i + 1)
                subset.pop(-1)
            return

        f(A, [], 0)
        return res


if __name__ == '__main__':
    s = Solution
    A = [1, 2, 3]
    print(s.solve(A))
