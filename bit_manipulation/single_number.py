class Solution:
    @staticmethod
    def single_num(A):
        ### below approach only works if the number is repeated times
        return sum(set(A))*2 - sum(A)


if __name__ == '__main__':
    s = Solution
    a = [4, 2, 1, 2, 1]
    print(s.single_num(a))
