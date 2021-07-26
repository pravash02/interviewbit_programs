class Solution:
    @staticmethod
    def excel_col_nbr(A):
        result = 0
        for i in range(0, len(A)):
            result *= 26
            result += ord(A[i]) - ord('A') + 1

        return result


if __name__ == '__main__':
    s = Solution
    num = 'AB'
    print(s.excel_col_nbr(num))
