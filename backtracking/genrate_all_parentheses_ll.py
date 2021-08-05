class Solution:

    @staticmethod
    def solve(n):
        def generate_recurr_parenthesis(n, paren, s, ans):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if paren != n:
                generate_recurr_parenthesis(n, paren + 1, s + '(', ans)

            if len(s) < 2 * paren:
                generate_recurr_parenthesis(n, paren, s + ')', ans)
        ans = []
        generate_recurr_parenthesis(n, 0, '', ans)
        return ans

    @staticmethod
    def solveB(A):
        def generate_recurr_parenthesisB(A, left, right, string, res):
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(string)
            if left > right:
                return
            generate_recurr_parenthesisB(A, left - 1, right, string + "(", res)
            generate_recurr_parenthesisB(A, left, right - 1, string + ")", res)

        res = []
        generate_recurr_parenthesisB(A, A, A, "", res)
        return res


if __name__ == '__main__':
    s = Solution
    n = 3
    print(s.solve(n))
    print(s.solveB(n))

