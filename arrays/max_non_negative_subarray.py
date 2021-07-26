class Solution:
    @staticmethod
    def maxset(A):
        max_set = []
        max_sum = -1
        cur_set = []

        for i in A:
            if (i >= 0):
                cur_set.append(i)
                cur_sum = sum(cur_set)
                if (cur_sum > max_sum):
                    max_sum = cur_sum
                    max_set = cur_set
            else:
                cur_set = []

        return max_set


if __name__ == '__main__':
    s = Solution
    lst = [10, -1, 2, 3, -4, 100]
    print(s.maxset(lst))
