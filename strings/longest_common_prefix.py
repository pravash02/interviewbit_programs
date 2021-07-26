class Solution:
    @staticmethod
    def long_prefix(A):
        A.sort()

        p = ''
        for i in range(min(len(A[0]), len(A[len(A) - 1]))):
            if A[0][i] == A[len(A) - 1][i]:
                p += str(A[0][i])

        return p

    @staticmethod
    def long_prefixB(A):
        res = A[0]  # final result
        for word in A:
            copy = word  # copy of the string
            while copy != res and res != "" and copy != "":
                if len(copy) > len(res):  # if copy is longer
                    copy = copy[:-1]  # remove last character
                else:
                    res = res[:-1]
            if res == "":
                break
        return res

    @staticmethod
    def long_prefixC(A):
        max_word_len = len(max(A))
        res = ""
        j = 0
        k = 0
        flag = 0
        temp_str = ''
        while k < max_word_len:
            for i in range(0, len(A)-1):
                if A[i][j] == A[i+1][j]:
                    temp_str = A[i][j]
                    flag = 1
                else:
                    flag = 0
                    break
            j += 1
            k += 1
            if flag == 0:
                break
            else:
                res += temp_str

        return ''.join(set(list(res)))


if __name__ == '__main__':
    s = Solution
    # A = ["abcdefgh", "aefghijk", "abcefgh"]
    A = ["abcd", "abcd", "efgh"]
    # print(s.long_prefix(A))
    # print(s.long_prefixB(A))
    print(s.long_prefixC(A))
