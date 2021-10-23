class Solution:
    def canJump(self, a):
        ans = ['F'] * len(a)
        n = len(a)
        if n == 1:
            return 1
        for i in range(n - 1, -1, -1):
            if i + a[i] >= n:
                ans[i] = 'T'
            else:
                k = i + 1
                while k <= i + a[i]:
                    if ans[k] == 'T':
                        ans[i] = 'T'
                    k += 1
        if ans[0] == 'T':
            return 1
        return 0

    def canJumpB(self, A):
        m = 0
        for i, el in enumerate(A):
            if m < i:
                return 0
            m = max(m, i + el)
        return 1


if __name__ == '__main__':
    s = Solution()
    A = [2, 3, 1, 1, 0, 4]
    print(s.canJump(A))
    print(s.canJumpB(A))
