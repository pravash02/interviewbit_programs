class Solution:
    @staticmethod
    def wave_array(A):
        A.sort()

        for i in range(0, len(A)-1):
            if i % 2 == 0:
                if A[i] < A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
            else:
                pass

        return A


if __name__ == '__main__':
    s = Solution
    lst = [1, 3, 4, 2, 5]
    print(s.wave_array(lst))
