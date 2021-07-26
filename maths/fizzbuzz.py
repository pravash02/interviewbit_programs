class Solution:
    @staticmethod
    def fizzbuzz(n):
        res = []
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(i)

        return res


if __name__ == '__main__':
    s = Solution
    n = 10
    print(s.fizzbuzz(n))
