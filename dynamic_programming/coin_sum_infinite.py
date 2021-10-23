class Solution:
    def coinchange2(self, A, B):
        m = len(A)
        table = [0] * (B + 1)
        table[0] = 1
        for j in range(m):
            for i in range(A[j], B + 1):
                table[i] += table[i - A[j]]

        print(table)
        return (table[B] % 1000007)


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3]
    B = 4
    print(s.coinchange2(A, B))
