class Solution:
    @staticmethod
    def bit_calc(A):
        bit_num = '{:032b}'.format(A)
        return bit_num.count('1')


    @staticmethod
    def bit_calcB(A):
        list_bit = []
        num = 0
        for i in range(33):
            num = 2 ** i
            list_bit.append(num)

        count = 0
        for i in reversed(list_bit):
            if A >= i:
                A = A - i
                count += 1

        return count


if __name__ == '__main__':
    s = Solution
    a = 11
    print(s.bit_calcB(a))
