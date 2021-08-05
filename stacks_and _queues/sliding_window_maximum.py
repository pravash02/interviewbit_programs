class Solution:
    @staticmethod
    def solve(A, B):
        res = []
        for i in range(0, len(A)-B+1):
            t = A[i]
            for j in range(i, i+B):
                if t < A[j]:
                    t = A[j]
            res.append(t)
        return res

    @staticmethod
    def solveB(A, B):
        res = []
        for i in range(0, len(A)-B+1):
            k = max(A[i:i+B])
            res.append(k)

        return res

    @staticmethod
    def solveC(A, B):
        ans = []
        m = A.index(max(A[:B]))

        if B >= len(A):
            return [max(A)]
        else:
            ans.append(A[m])
            for i in range(B, len(A)):
                if (i - m) < B:
                    if A[i] >= A[m]:
                        ans.append(A[i])
                        m = i
                    else:
                        ans.append(A[m])
                else:
                    C = A[i - B + 1:i + 1]
                    m = C.index(max(C)) + (i - B + 1)
                    ans.append(A[m])

        return ans


if __name__ == '__main__':
    s = Solution
    A = [4, 5, 2, 10, 8, 2, 5, 7, 10]
    B = 3
    print(s.solve(A, B))
    print(s.solveB(A, B))
