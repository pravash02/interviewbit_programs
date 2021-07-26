class Solution:
    @staticmethod
    def pow(x, n, d):
        ### x^n % d
        if d == 1:
            return 0
        elif x == 0:
            return x
        elif n == 0:
            return 1
        elif n == 1:
            return x % d

        r = x % d
        oddP = []
        while n >= 2:
            if n % 2 == 1:
                oddP.append(r)
            r = (r * r) % d
            n //= 2
        for i in oddP:
            r = (r * i) % d
        return r

    @staticmethod
    def powB(x, n, d):
        if n % 2 == 0:
            return ((x ** (n // 2)) * (x ** (n // 2))) % d
        else:
            return (x * ((x ** (n // 2)) * (x ** (n // 2)))) % d

    @staticmethod
    def powC(x, n, d):
        res = 1
        while n > 0:
            if n % 2 == 1:
                res = res * x
                res = res % d

            n = n // 2
            x = x * x
            x = x % d

        res = res % d
        return res


if __name__ == '__main__':
    s = Solution
    x = 2
    n = 3
    d = 3
    print(s.pow(x, n, d))
