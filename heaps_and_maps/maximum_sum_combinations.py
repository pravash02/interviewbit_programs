from heapq import heapify, heappop, heappush


class Solution:
    @staticmethod
    def solve(A, B, C):
        A.sort()
        B.sort()

        seen, pq, result = set(), list(), list()
        i, j = len(A) - 1, len(A) - 1
        seen.add((i, j))
        pq.append((-(A[i] + A[j]), (i, j)))
        for _ in range(C):
            sum, (i, j) = heappop(pq)
            result.append(-sum)
            for ni, nj in [(i - 1, j), (i, j - 1)]:
                if ni >= 0 and nj >= 0 and (ni, nj) not in seen:
                    heappush(pq, (-(A[ni] + A[nj]), (ni, nj)))
                    seen.add((ni, nj))

        return result


if __name__ == '__main__':
    s = Solution
    A = [3, 2]
    B = [1, 4]
    C = 2
    print(s.solve(A, B, C))
