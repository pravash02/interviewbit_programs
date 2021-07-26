class Solution:
    @staticmethod
    def excel_col_title(A):
        result = ""
        while A > 0:
            c = chr(ord('A') + (A-1) % 26)
            result = c + result
            A = (A-1) // 26

        return result


if __name__ == '__main__':
    s = Solution
    num = 28
    print(s.excel_col_title(num))
