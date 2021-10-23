import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
class Solution:
    # @param A : string
    # @return an integer
    @lru_cache(100000)
    def minCut(self, s):
        return 0 if s[::-1] == s else min(1 + self.minCut(s[i:]) for i in range(1, len(s)) if s[:i][::-1] == s[:i])


if __name__ == '__main__':
    s = Solution()
    A = 'abcba'
    print(s.minCut(A))
