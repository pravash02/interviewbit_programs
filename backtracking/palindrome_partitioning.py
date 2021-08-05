class Solution:

    @staticmethod
    def solve(A):
        def is_pan(s):
            return s == s[::-1]

        def f(s, path):
            if not s:
                res.append(path)
                return

            for i in range(1, len(s) + 1):
                if is_pan(s[:i]):
                    print(path + [s[:i]])
                    f(s[i:], path + [s[:i]])
            return

        res = []
        f(A, [])
        return res


if __name__ == '__main__':
    s = Solution
    A = '23432'
    print(s.solve(A))
