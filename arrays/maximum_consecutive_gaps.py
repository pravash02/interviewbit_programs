class Solution:
    @staticmethod
    def maximum_gap(A):
        A.sort()

        i = 0
        max_diff = 0

        while i < len(A) - 1:
            cur_diff = abs(A[i+1] - A[i])
            if cur_diff > max_diff:
                    max_diff = cur_diff

            i += 1

        return max_diff


if __name__ == '__main__':
    s = Solution
    lst = [1, 10, 5]
    # lst2 = [2, 3, 10, 6, 4, 8, 1]
    print(s.maximum_gap(lst))
