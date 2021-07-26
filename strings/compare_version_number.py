class Solution:
    @staticmethod
    def compare(A, B):
        lst_a = A.split('.')
        lst_b = B.split('.')

        len_a = len(lst_a)
        len_b = len(lst_b)
        if len_a > len_b:
            diff = len_a - len_b
            lst_b.extend(['0'] * diff)
        else:
            diff = len_b - len_a
            lst_a.extend(['0'] * diff)

        for i in range(0, len_a):
            if int(lst_a[i]) != int(lst_b[i]):
                if int(lst_a[i]) > int(lst_b[i]):
                    return 1
                else:
                    return -1

        return 0

    @staticmethod
    def compareB(A, B):
        A = list(map(int, A.split('.')))
        B = list(map(int, B.split('.')))
        while (len(A) < len(B)):
            A.append(0)
        while (len(B) < len(A)):
            B.append(0)
        for i in range(len(A)):
            if A[i] < B[i]:
                return -1
            if B[i] < A[i]:
                return 1
        return 0


if __name__ == '__main__':
    s = Solution
    a = "7.5.2.4"
    b = "7.5.3"
    print(s.compare(a, b))
