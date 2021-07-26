class Solution:
    @staticmethod
    def solve(A):
        # Base case
        if len(A) == 1:
            return [A]

        # Recursive call
        ans = []
        for elem in A:
            # 1. collect list of answers from sub list
            rest = [e for e in A if e != elem]
            heads = Solution.solve(rest)    # for 1, it return [2,3] [3,2]
            # 2. append current element to every sublist
            for l in heads:
                l.append(elem)
            # 3. concatenate answers for all elems
            ans = ans + heads

        return ans

    @staticmethod
    def solveB(A):
        import itertools
        res = itertools.permutations([1, 2, 3])
        ans = []
        for i in res:
            ans.append(list(i))

        return ans


if __name__ == '__main__':
    s = Solution
    A = [1, 2, 3]
    print(s.solve(A))
    print(s.solveB(A))
