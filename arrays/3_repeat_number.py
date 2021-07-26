class Solution:
    @staticmethod
    def majority_elem(A):
        d = {}
        count = 1
        n = len(A)

        for i in range(0, len(A)):
            if A[i] in d:
                d[A[i]] = d[A[i]] + count
            else:
                d[A[i]] = count

            if d[A[i]] > n // 3:
                return A[i]

        return -1

    ## Moore's Voting Algorithm
    @staticmethod
    def majority_elemB(A):
        n = len(A)
        count = 0
        major_index = 0

        for i in range(1, n):
            if A[i] == A[major_index]:
                count += 1
            else:
                count -= 1
            if count == 0:
                A[major_index] = i
                count += 1

        count = 0
        for i in range(0, n):
            if A[i] == A[major_index]:
                count += 1
        if count > n // 2:
            return A[major_index]

        return -1

    @staticmethod
    def majority_elemC(A):
        n = len(A)
        ele1 = ele2 = float('inf')
        count1 = count2 = 0
        for i in range(0, n):
            if ele1 == A[i]:
                count1 += 1
            elif ele2 == A[i]:
                count2 += 1
            elif count1 == 0:
                ele1 = A[i]
                count1 += 1
            elif count2 == 0:
                ele2 = A[i]
                count2 += 1
            else:
                count1 -= 1
                count1 -= 1

        count1 = count2 = 0
        for i in range(0, len(A)):
            if ele1 == A[i]:
                count1 += 1
            elif ele2 == A[i]:
                count2 += 1
        if count1 > n // 3:
            return ele1
        if count2 > n // 3:
            return ele2

        return -1


if __name__ == '__main__':
    s = Solution
    lst = [1, 1, 2, 5, 1]
    print(s.majority_elemB(lst))
