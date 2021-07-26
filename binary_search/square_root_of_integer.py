class Solution:
    @staticmethod
    def sqrt_int(A):
        start = 0
        end = A + 1
        ans = 0
        while end - start > 1:
            mid = (end + start) // 2

            if (mid * mid) <= A:
                ans = mid
                start = mid
            else:
                end = mid

        return ans


if __name__ == '__main__':
    s = Solution
    x = 11
    print(s.sqrt_int(11))
