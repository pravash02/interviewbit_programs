class Solution:
    @staticmethod
    def missing_int(A):
        A.sort()
        count = i = 0
        size_arr = len(A)

        while i < size_arr:
            if A[i] < 0:
                pass
            if A[i] == 0:
                z = A.pop(i)
                A.append(i)
                i -= 1
            elif A[i + 1] - A[i] == 1:
                pass
            else:
                if A[i + 1] - A[i] <= 0 or A[i] < 0:
                    pass
                else:
                    return A[i] + 1
            i += 1

    @staticmethod
    def missing_intB(A):
        size_arr = len(A)
        i = 0
        while i < size_arr:
            if A[i] > 0 and A[i] <= size_arr:
                pos = A[i] - 1
                if A[pos] != A[i]:
                    A[pos], A[i] = A[i], A[pos]
                    i -= 1
            i += 1

        for i in range(0, size_arr):
            if A[i] != i + 1:
                return i + 1

        return size_arr + 1


    @staticmethod
    def missing_intC(A):
        A = set(A)
        i = 1
        while True:
            if i not in A:
                return i
            i = i + 1


if __name__ == '__main__':
    s = Solution
    lst = [3, 4, -1, 1, 0]
    lst2 = [3, 4, -1, 1]
    lst3 = [1, 2, 0]
    print(s.missing_intC(lst3))
