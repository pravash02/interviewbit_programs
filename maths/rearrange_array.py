class Solution:
    @staticmethod
    def rearrange_arr(A):
        lst = []
        for i in range(0, len(A)):
            lst.append(A[A[i]])

        print(lst)

    ## O(1) extr space that is modifying using the same list
    @staticmethod
    def rearrange_arrB(A):
        N = len(A)
        for i in range(len(A)):
            A[i] = A[i] + N * (A[A[i]] % N)
        for i in range(len(A)):
            A[i] = A[i] // N

        return A


if __name__ == '__main__':
    s = Solution
    n = [3, 2, 4, 1, 0]
    print(s.rearrange_arr(n))
