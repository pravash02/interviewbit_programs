class Solution:

    @staticmethod
    def intToRoman(A):
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
                    "V", "IV", "I"]

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        if A > 1 and A > 3999:
            return ""

        i = 0
        res = ""
        while A > 0:
            if A - values[i] >= 0:
                res += numerals[i]
                A = A - values[i]
            else:
                i += 1

        return res
