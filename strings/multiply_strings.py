class Solution:
    @staticmethod
    def multiply_strings(A, B):
        return str(int(A) * int(B))


if __name__ == '__main__':
    s = Solution
    a = '12'
    b = '10'
    print(int(a))
    print(s.multiply_strings(a, b))
