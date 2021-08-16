class Solution:
    @staticmethod
    def solve(A, B):
        d = {}
        ans = 0
        for i in A:
            x = i ^ B
            if x in d:
                ans += 1

            d[i] = 1

        return ans


if __name__ == '__main__':
    s = Solution
    A = [5, 4, 10, 15, 7, 6]
    B = 5
    print(s.solve(A, B))
