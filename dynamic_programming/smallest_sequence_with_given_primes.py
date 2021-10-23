import heapq


class Solution:

    def solve(self, A, B, C, D):
        h, res = [], []
        for elem in [A, B, C]:
            if elem not in h:
                heapq.heappush(h, elem)

        while len(res) < D:
            min_ele = heapq.heappop(h)
            res.append(min_ele)
            for elem in [min_ele * A, min_ele * B, min_ele * C]:
                if elem not in h:
                    heapq.heappush(h, elem)

        return res