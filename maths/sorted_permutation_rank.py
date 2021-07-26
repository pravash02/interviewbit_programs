import math


class Solution:
    @staticmethod
    def srt_perm(A):
        x = [t for t in A]
        x.sort()
        i = 0
        r = 0
        while x:
            r = r + (x.index(A[i]) * math.factorial(len(x) - 1))
            x.remove(A[i])
            i = i + 1

        return (r + 1) % 1000003

    @staticmethod
    def srt_permB(A):
        A = list(A)
        chars = sorted(A)
        count = 1
        i = 0
        while i < len(A):
            index = chars.index(A[i])
            if index != 0:
                ### starting index from 1 for finding the factorial
                count += math.factorial(len(A) - i - 1) * index
            else:
                if chars[i:] == A[i:]:
                    break
            chars.pop(index)
            A.pop(i)

        return (count) % 1000003


if __name__ == '__main__':
    s = Solution
    a = 'acb'
    print(s.srt_permB(a))
