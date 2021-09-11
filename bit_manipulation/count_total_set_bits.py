import math


class Solution:
    @staticmethod
    ### using logarithmic approach
    def count_bitsA(A):
        return int(math.log(A, 2) + 1)

    @staticmethod
    def count_bitsB(A):
        count = 0
        while A:
            count += 1
            A >>= 1

        return count

    @staticmethod
    def count_bitsC(n):
        x = n
        k = 0
        while (x > 0):
            x = x >> 1
            k += 1
        n += 1
        x = 2
        s = 0
        for i in range(k):
            p = x // 2
            s += (n // x) * p
            v = (n % x) - (p)
            if v > 0:
                s += v
            x = x << 1
            s = s % 1000000007
        return s


if __name__ == '__main__':
    s = Solution
    a = 27
    print(s.count_bitsC(a))
