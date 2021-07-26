class Solution:
    @staticmethod
    def noble_array(A):
        A.sort()
        temp_val = -1

        for i in range(0, len(A) - 1):
            if A[i] == A[i + 1]:
                continue

            # main logic
            if A[i] == len(A) - 1 - i:
                temp_val = i

            if A[i] == A[len(A) - 1]:
                return -1

        if A[-1] == 0:
            return 1

        if temp_val != -1:
            return 1
        else:
            return -1


if __name__ == '__main__':
    s = Solution
    lst = [10, 3, 20, 40, 2]
    print(s.noble_array(lst))
