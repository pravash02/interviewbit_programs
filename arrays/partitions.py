class Solution:
    @staticmethod
    def partitions(A, B):
        lst_sum = sum(B)
        if (lst_sum % 3) != 0:
            return 0

        one_third_sum = lst_sum // 3
        two_third_count = 2*one_third_sum

        count = 0
        one_third_count = 0
        cummilative_sum = 0

        for i in range(0, len(B)-1):
            cummilative_sum += B[i]

            if cummilative_sum == two_third_count:
                count += one_third_count

            if cummilative_sum == one_third_sum:
                one_third_count += 1

        return count


if __name__ == '__main__':
    s = Solution
    lst = [1, 2, 3, 0, 3]
    print(s.partitions(len(lst), lst))
