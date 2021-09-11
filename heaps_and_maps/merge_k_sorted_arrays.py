import heapq


class Solution:
    @staticmethod
    def solve(A):
        arr = A
        n = len(arr)
        new = []
        for x in arr:
            new += x
        print(new)
        heapq.heapify(new)
        ans = []
        for x in range(len(new)):
            ans.append(heapq.heappop(new))
        return ans

    # interviewbit solution
    @staticmethod
    def solveB(A):
        arr = A
        k = len(arr[0])
        m = len(arr)
        q = []
        ans = []
        for i in range(m):
            heapq.heappush(q, (arr[i][0], i, 0))
        while q != []:
            top = heapq.heappop(q)
            ans.append(top[0])
            if top[2] == k - 1:
                continue
            x = top[1]
            y = top[2] + 1
            heapq.heappush(q, (arr[x][y], x, y))
        return ans


if __name__ == '__main__':
    s = Solution
    A = [
             [1, 2, 3],
             [2, 4, 6],
             [0, 9, 10]
             ]
    print(s.solve(A))
    print(s.solveB(A))
