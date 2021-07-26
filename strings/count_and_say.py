class Solution:
    @staticmethod
    def count_seq(A):
        seq = []
        for i in range(0, A):
            if i == 0:
                seq.append(str(1))
            if i == 1:
                seq.append(str(11))
            if i >= 2:
                count = 0
                num = str(seq[-1])
                next_str = ''
                k = 0
                while k in range(0, len(num)):
                    j = num[k]
                    while k < len(num):
                        if j == num[k]:
                            count += 1
                            k += 1
                        else:
                            next_str += str(count) + str(j)
                            count = 0
                            break

                        if len(num) == k:
                            next_str += str(count) + str(j)
                            break

                seq.append(next_str)

        return seq[-1]


    @staticmethod
    def count_seqB(A):
        def next_num(s):
            result, i, size = [], 0, len(s) - 1
            while i <= size:
                count = 1
                while (i + 1 <= size and s[i] == s[i + 1]):
                    i += 1
                    count += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)

        s = '1'
        for i in range(1, A):
            s = next_num(s)

        return s


if __name__ == '__main__':
    s = Solution
    a = 6
    print(s.count_seq(a))
