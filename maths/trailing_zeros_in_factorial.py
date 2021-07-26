class Solution:
    @staticmethod
    def factorial(A):
        if A == 0 or A == 1:
            return 1
        else:
            return A * Solution.factorial(A-1)

    @staticmethod
    def trail_zeros(A):
        fact_int = Solution.factorial(A)

        zero_count = 0
        while fact_int > 0:
            zero_int = fact_int % 10
            if zero_int == 0:
                zero_count += 1
            else:
                break
            fact_int = fact_int // 10

        return zero_count


    ### log time complexity
    @staticmethod
    def trail_zerosB(A):
        n = 5
        count = 0

        while n <= A:
            count += A//n
            n *= 5

        return count


if __name__ == '__main__':
    s = Solution
    num = 5
    print(s.trail_zerosB(num))
