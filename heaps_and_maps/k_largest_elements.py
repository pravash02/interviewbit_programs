import heapq


class Solution:
    @staticmethod
    def solve(A, B):
        heapq.heapify(A)
        return heapq.nlargest(B, A)

    @staticmethod
    def solveB(A, B):
        l1 = []
        A.sort(reverse=True)
        for i in range(B):
            l1.append(A[i])
        return l1


if __name__ == '__main__':
    s = Solution
    A = [11, 3, 4]
    B = 2
    print(s.solveB(A, B))
