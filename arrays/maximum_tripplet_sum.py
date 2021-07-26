import copy


class Solution:
    @staticmethod
    def max_tripplet_sumA(A):
        s = max_sum = 0

        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                for k in range(j + 1, len(A)):
                    s = A[i] + A[j] + A[k]

                    if s > max_sum:
                        max_sum = s

        return max_sum

    @staticmethod
    def max_tripplet_sumB(A):
        s = max_sum = 0
        B = A.copy()
        A.sort()

        for i in range(0, len(B) - 1):
            j = i + 1
            k = len(B) - 1
            while j < k:
                # s = B[i] + B[j] + B[k]
                if B[i] < B[j] < B[k] and 0 <= i < j < k:
                    print(B[i], B[j], B[k])
                    # if 0<=B.index(A[i]) < B.index(A[j]) < B.index(A[k]) and B[B.index(A[i])] < B[B.index(A[j])] < B[B.index(A[k])]:
                    # s = A[i] + A[j] + A[k]
                    s = B[i] + B[j] + B[k]
                    if s > max_sum:
                        print(s)
                        max_sum = s

                j += 1
                k -= 1

        if max_sum > 0:
            return max_sum
        else:
            return 0


if __name__ == '__main__':
    s = Solution
    lst = [1, 2, 3, 0, -1, 8, 10]  # 21
    lst2 = [18468, 6335, 26501, 19170, 15725, 11479, 29359, 26963, 24465, 5706, 28146, 23282, 16828, 9962, 492, 2996,
            11943, 4828, 5437, 32392, 14605]
    # print(s.max_tripplet_sumA(lst))
    print(s.max_tripplet_sumB(lst2))  # 88252
