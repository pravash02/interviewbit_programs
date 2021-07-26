class Solution:
    @staticmethod
    def next_perm(A):
        max_nbr = -1
        ind = new_ind = -1

        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                max_nbr = A[i]
            else:
                ind = i
                break

        ## return sorted array if no permutations are possible
        if ind == -1:
            return sorted(A)

        for j in range(len(A) - 1, ind, -1):
            if A[j] > A[ind]:
                A[ind], A[j] = A[j], A[ind]
                break

        return A[:ind+1] + sorted(A[ind+1:])

    @staticmethod
    def next_permB(A):
        n = len(A)
        ind = -1
        for i in range(0, n - 1):
            if A[i] < A[i + 1]:
                ind = i

        if ind == -1:
            return sorted(A)

        for j in range(n - 1, ind, -1):
            if A[j] > A[ind]:
                A[ind], A[j] = A[j], A[ind]
                break

        return A[:ind + 1] + list(reversed(A[ind + 1:]))


if __name__ == '__main__':
    s = Solution
    lst = [100, 40, 60, 70, 90, 85, 80, 10]
    print(s.next_perm(lst))
    print(s.next_permB(lst))
