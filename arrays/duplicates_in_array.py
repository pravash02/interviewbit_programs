class Solution:
    @staticmethod
    def repeated_number(A):
        d = {}
        count = 1

        for i in range(0, len(A)):
            if A[i] in d.keys():
                d[A[i]] = d[A[i]] + count
                return A[i]
            else:
                d[A[i]] = count

        return -1


if __name__ == '__main__':
    s = Solution
    lst = [3, 4, 1, 3]
    print(s.repeated_number(lst))
