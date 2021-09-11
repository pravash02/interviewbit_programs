import heapq


class Solution:
    @staticmethod
    def solve(A, B):
        res = 0
        while B > 0:
            temp = max(A)
            i = A.index(temp)
            A[i] = A[i] - 1
            res += temp
            B -= 1
        return res

    @staticmethod
    def solveB(A, B):
        heap = [-1 * c for c in A]
        heapq.heapify(heap)
        s = 0
        while B > 0:
            d = heapq.heappop(heap)
            s += d * -1
            heapq.heappush(heap, d + 1)
            B -= 1
        return s


if __name__ == '__main__':
    s = Solution
    A = [2, 3]
    B = 3
    print(s.solve(A, B))
