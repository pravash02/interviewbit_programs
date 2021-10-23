class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        d = {}

        def solve(s):
            if s in d:
                return d[s]
            ans = []
            for w in B:
                if s[:len(w)] == w:
                    if len(s) == len(w):
                        ans.append(w)
                    else:
                        temp = solve(s[len(w):])
                        for t in temp:
                            ans.append(w + " " + t)

            d[s] = sorted(list(set(ans)))
            return d[s]

        return solve(A)


if __name__ == '__main__':
    s = Solution()
    A = "myinterviewtrainer"
    B = ["interview", "my", "trainer"]
    print(s.wordBreak(A, B))
