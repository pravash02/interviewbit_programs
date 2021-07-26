from functools import cmp_to_key as cmp


class Solution:
    @staticmethod
    def largest_numA(A):
        if all(A) == 0:
            return 0

        A.sort(key=cmp(lambda x, y: 1 if int(str(x) + str(y)) >= int(str(y) + str(x)) else -1), reverse=True)
        s = ""
        for ele in A:
            s += str(ele)
        if s[0] == '0':
            return 0

        return s

    @staticmethod
    def largest_numB(A):
        if all(A) == 0:
            return 0

        for i in range(0, len(A) - 1):
            j = i + 1
            while j < len(A):
                AB = str(A[i]) + str(A[j])
                BA = str(A[j]) + str(A[i])

                if int(BA) > int(AB):
                    A[j], A[i] = A[i], A[j]
                j += 1

        return "".join(str(i) for i in A)

    @staticmethod
    def largest_numC(A):
        maxsize = minsize = 1
        for x in A:
            maxsize = max(maxsize, len(str(x)))
            minsize = min(minsize, len(str(x)))
            print(str(x), len(str(x)), maxsize, minsize)
        return str(int(''.join(sorted(map(str, A), key=lambda s: s * (maxsize // minsize))[::-1])))


if __name__ == '__main__':
    s = Solution
    lst = [3, 30, 34, 9]
    lst2 = [0, 0, 0, 0, 0]
    print(s.largest_numB(lst))
