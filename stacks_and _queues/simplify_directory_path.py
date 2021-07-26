class Solution:
    @staticmethod
    def solve(A):
        A = A + '/'
        l = A.split('/')
        m = ['/']       # for handling base case
        for i in range(1, len(l) - 1):
            if l[i] == ".." and len(m) > 1:
                m.pop()
            elif l[i] == ".." and len(m) == 1:
                continue
            elif l[i] == ".":
                continue
            elif l[i] != '':
                m.append('/' + str(l[i]))
        if len(m) == 1:
            return '/'

        return (''.join(m))[1:]

    @staticmethod
    def solveB(A):
        x = A.split("/")
        res = []
        ch = ['.', '..', "''"]
        for i in range(len(x)):
            if x[i] not in ch:
                res.append(x[i])

            elif x[i] == "..":
                if res:
                    res.pop()

        return "/".join(res)


if __name__ == '__main__':
    s = Solution
    A = "/a/./b/../../c/"
    print(s.solve(A))
    print(s.solveB(A))
