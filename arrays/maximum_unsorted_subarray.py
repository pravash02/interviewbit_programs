class Solution:
    @staticmethod
    def unsorted_subarray(A):
        min_start = max_end = -1
        pos_lst = []

        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                min_start = i
                break

        # array is sorted
        if min_start == -1:
            return -1

        for i in range(len(A)-1, -1, -1):
            if A[i] < A[i-1]:
                max_end = i
                break

        minval = maxval = float('-inf')
        for i in range(min_start, max_end):
            minval = min(A[i], minval)
            maxval = max(A[i], maxval)

        for i in range(0, min_start-1):
            if A[i] > minval:
                min_start = i
                break

        for i in range(max_end+1, len(A)-1):
            if A[i] < maxval:
                max_end = i
                break

        pos_lst.append(min_start)
        pos_lst.append(max_end)
        return pos_lst

    @staticmethod
    def unsorted_subarrayB(A):
        l = sorted(A)
        st, end = -1, -1
        for i in range(len(A)):
            if l[i] == A[i]:
                continue
            elif st == -1:
                st = i
            else:
                end = i
        if st == -1 and end == -1:
            return [-1]

        return [st, end]


if __name__ == '__main__':
    s = Solution
    lst = [1, 3, 2, 5, 6]
    lst2 = [1, 2, 3]
    print(s.unsorted_subarrayB(lst2))
