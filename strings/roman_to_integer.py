class Solution:
    @staticmethod
    def roman_to_int(A):
        data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        count = 0
        i = 0
        while i < len(A) - 1:

            if data[A[i + 1]] > data[A[i]]:
                count += data[A[i + 1]] - data[A[i]]
                i += 2

            else:
                count += data[A[i]]
                i += 1

        if i != len(A):
            return count + data[A[-1]]

        return count


if __name__ == '__main__':
    s = Solution
    M = "MMCDLXXV"
    print(s.roman_to_int(M))
