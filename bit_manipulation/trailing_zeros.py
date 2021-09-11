class Solution:
    @staticmethod
    def trailing_zero(A):
        b = bin(A)
        # print(b[::-1])
        count = 0
        for i in b[::-1]:
            if i == '0':
                count += 1
            if i == '1':
                break

        return count


if __name__ == '__main__':
    s = Solution
    a = 18
    print(s.trailing_zero(a))
