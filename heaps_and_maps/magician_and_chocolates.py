import heapq


class Solution:
    @staticmethod
    def solve(A, B):
        count = 0
        if len(B) == 0:
            return 0
        B = [-x for x in B]
        heapq.heapify(B)
        while A > 0:
            t = heapq.heappop(B)
            print(t)
            count += t
            heapq.heappush(B, -1 * (-1 * t // 2))
            A -= 1
        return (-1 * count) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution
    A = 3
    B = [6, 5]
    print(s.solve(A, B))
