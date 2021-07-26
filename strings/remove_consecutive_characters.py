class Solution:
    @staticmethod
    def rmv_char(A, B):
        ans = []
        for i in A:
            ans.append(i)

        i = 0
        while i < len(ans):
            cnt = ans.count(ans[i])
            if cnt == B:
                ans.remove(ans[i])
                i -= 1
            i += 1

        return ''.join(i for i in ans)

    @staticmethod
    def rmv_charB(A, B):
        import re
        pattern = "a+"
        for i in range(98, 98 + 25):
            pattern += "|" + chr(i) + "+"
        return "".join(filter(lambda x: len(x) != B, re.findall(pattern, A)))


if __name__ == '__main__':
    s = Solution
    A = 'PAYPALISHIRING'
    B = 2
    print(s.rmv_char(A, B))
    print(s.rmv_charB(A, B))
