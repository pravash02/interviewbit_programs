from collections import defaultdict


class Solution:
    @staticmethod
    def solve(A):
        longestSubL, idxFollowup = 0, defaultdict(str)
        n, recordedIdx, tempL = len(A), 0, 0
        if n <= 1: return n
        for i in range(1, n + 1):
            if idxFollowup[A[i - 1]] == "":
                pass
            elif recordedIdx <= idxFollowup[A[i - 1]]:
                recordedIdx = idxFollowup[A[i - 1]]
            tempL = i - recordedIdx
            # update string idx
            idxFollowup[A[i - 1]] = i
            if longestSubL < tempL:
                longestSubL = tempL
        return longestSubL

    @staticmethod
    def solveB(A):
        start = 0
        max_len = 0
        char_location_map = {}
        for i, char in enumerate(A):
            if char in char_location_map and char_location_map[char] >= start:
                max_len = max(max_len, i - start)
                start = char_location_map[char] + 1
            char_location_map[char] = i
        return max(max_len, i - start + 1)


if __name__ == '__main__':
    s = Solution
    A = 'aaabcbce'
    print(s.solve(A))
    print(s.solveB(A))
