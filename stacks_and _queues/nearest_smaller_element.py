class Solution:
    @staticmethod
    def solve(A):
        ans = []
        smallest = 0
        for i in range(len(A)):
            if A[i] > A[smallest]:
                for j in range(i - 1, smallest - 1, -1):
                    if A[j] < A[i]:
                        ans.append(A[j])
                        break
            else:
                ans.append(-1)
                smallest = i

        return ans

    @staticmethod
    def solveB(A):
        G = []
        for i in range(len(A)):
            while (len(G) > 0 and G[-1] >= A[i]):
                G.pop()
            x = G[-1] if len(G) > 0 else -1
            G.append(A[i])
            A[i] = x
        return A

    @staticmethod
    def solveC(A):
        s = []
        G = []
        for i in range(len(A)):
            if not s:
                G.append(-1)
            elif s and s[-1] < A[i]:
                G.append(s[-1])
            elif s and s[-1] >= A[i]:
                while s and s[-1] >= A[i]:
                    s.pop()
                if not s:
                    G.append(-1)
                else:
                    G.append(s[-1])

            s.append(A[i])
        return G


if __name__ == '__main__':
    s = Solution
    A = [4, 5, 2, 10, 8]
    print(s.solveC(A))
