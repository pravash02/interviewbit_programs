class Solution:
    @staticmethod
    def solve(A, B):
        ans = 0
        zeros = []
        zn = 0
        n = len(A)
        for i in range(n):
            if A[i] == 0:
                zeros.append(i)
                zn += 1
            if zn <= B:
                ans = max(ans, i + 1)
            else:
                ans = max(ans, i - zeros[zn - 1 - B])
        return ans

    ### sliding window algorithm
    @staticmethod
    def solveB(A, B):
        ones = 0
        zeros = 0
        start = 0
        result = 0

        for i in range(len(A)):
            if A[i] == 1:
                ones += 1
            elif A[i] == 0:
                zeros += 1

            while zeros > B:
                if A[start] == 1:
                    ones -= 1
                else:
                    zeros -= 1
                start += 1
            result = max(result, ones+zeros)

        return result

    @staticmethod
    def solveC(A, B):
        ans = 0
        zeros = 0
        n = len(A)
        j = 0
        for i in range(n):
            if A[i] == 0:
                zeros += 1

            while zeros > B:
                if A[j] == 0:
                    zeros -= 1
                j += 1
            ans = max(ans, i-j+1)

        return ans


if __name__ == '__main__':
    s = Solution
    A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    B = 2
    print(s.solve(A, B))
    print(s.solveB(A, B))
    print(s.solveC(A, B))
