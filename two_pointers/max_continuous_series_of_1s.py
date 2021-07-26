class Solution:
    @staticmethod
    def solve(A, B):
        res = k = p = 0
        start = zeros = 0
        ind_lst = []
        for i in range(len(A)):
            if A[i] == 0:
                zeros += 1

            while zeros > B:
                if A[start] == 0:
                    zeros -= 1
                start += 1

            if res < i-start+1:
                res = i-start+1
                k = i
                p = start

        for j in range(p, k+1):
            ind_lst.append(j)

        return ind_lst


if __name__ == '__main__':
    s = Solution
    A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    A1 = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    B = 2
    print(s.solve(A, B))
