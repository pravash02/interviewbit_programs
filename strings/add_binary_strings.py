class Solution:
    @staticmethod
    def add_bin(A, B):
        a = int(A, 2)
        b = int(B, 2)

        su = bin(a+b).replace('0b', '')
        return su


if __name__ == '__main__':
    s = Solution
    a = '100'
    b = '11'
    print(s.add_bin(a, b))
