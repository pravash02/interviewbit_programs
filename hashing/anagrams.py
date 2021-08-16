from collections import defaultdict


class Solution:
    @staticmethod
    def solve(A):
        # A = list(A)
        # for i in range(len(A)):
        #     A[i] = "".join(list(sorted(list(A[i]))))
        temp = [str(sorted(list(A[i]))) for i in range(len(A))]
        dict = {}
        for i in range(len(temp)):
            if temp[i] in dict:
                dict[temp[i]].append(i + 1)
            else:
                dict[temp[i]] = [i + 1]
        return list(dict.values())

    @staticmethod
    def solveB(A):
        groups = defaultdict(list)

        for i in range(len(A)):
            groups[tuple(sorted(A[i]))].append(i + 1)

        return list(groups.values())


if __name__ == '__main__':
    s = Solution
    A = ['cat', 'dog', 'god', 'tca']
    print(s.solve(A))
    print(s.solveB(A))
