class Solution:
    def strongPasswordChecker(self, s: str):
        missing_type = 3
        if any("a" < c < "z" for c in s): missing_type -= 1
        if any("A" < c < "Z" for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1

        n = len(s)
        # change: to fix seq of three or more, number of changes needed
        # one: # of seq 3k
        # two: # of seq 3k + 1
        change = one = two = 0
        i = 2
        while i < n:
            if s[i] == s[i-1] == s[i-2]:
                l = 2
                while i < n and s[i] == s[i-1]:
                    i += 1
                    l += 1
                if l % 3 == 0:
                    one += 1
                if l % 3 == 1:
                    two += 1
                change += l // 3
            else:
                i += 1

        if n < 6:
            return max(6 - n, missing_type)
        elif n <= 20:
            return max(change, missing_type)
        else:
            delete = n - 20 # mininum delete needed
            change -= min(delete, one) # every delete, change can reduce by one
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
            return delete + max(missing_type, change)


if __name__ == '__main__':
    s = Solution()
