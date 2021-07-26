class Solution:
    @staticmethod
    def min_value(A):
        global_val = float('inf')
        A.sort()

        for i in range(0, len(A)-1):
            min_val = min(global_val, (A[i] ^ A[i+1]))

            if min_val < global_val:
                global_val = min_val

        return global_val


if __name__ == '__main__':
    s = Solution
    a = [0, 4, 7, 9]
    print(s.min_value(a))
