class Solution:
    @staticmethod
    def reverse_bits(A):
        bit_num = '{:032b}'.format(A)
        return int(str(bit_num)[::-1], 2)

    @staticmethod
    def reverse_bitsB(A):
        b = 0
        for i in range(0, 32):
            b <<= 1
            b = b | (A & 1)
            A >>= 1
        return b


if __name__ == '__main__':
    s = Solution
    a = 3
    print(s.reverse_bitsB(a))
