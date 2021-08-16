from collections import Counter


class Solution:
    @staticmethod
    def solve(A, B):
        n = len(A)
        ans = 0
        for i in range(n - 1):
            for j in range(n, i + 2, -1):
                c1 = A[i:j].count(1)
                c0 = A[i:j].count(0)
                if c1 - c0 == 1:
                    ans = max(ans, j - i + 1)

        return ans

    @staticmethod
    def solveB(A, B):
        n = len(A)
        output = []
        if B > n:
            return output
        counter = Counter(A[:B])
        output.append(len(counter))
        for i in range(B, n):
            counter[A[i - B]] -= 1
            counter[A[i]] += 1
            if counter[A[i - B]] == 0:
                counter.pop(A[i - B])
            output.append(len(counter))
        return output


if __name__ == '__main__':
    s = Solution
    A = [1, 2, 1, 3, 4, 3]
    B = 3
    # print(s.solve(A, B))
    print(s.solveB(A, B))
