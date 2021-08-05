class Solution:

    @staticmethod
    def solve(A):
        d = {'0': '0', '1': '1', '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

        if not A:
            return ''

        if len(A) == 1:
            return d[A[0]]

        s = ''
        res = []

        for ch in d[A[0]]:
            for x in Solution.solve(A[1:]):
                s = ch + x
                res.append(s)
                s = ''

        return res


if __name__ == '__main__':
    s = Solution
    A = '234'
    print(s.solve(A))
