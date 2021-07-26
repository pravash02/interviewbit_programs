class Solution:
    @staticmethod
    def flip(A):
        count = 0
        max_count = 0
        left_ind = -1   # min value
        right_ind = -1  # min value
        fnl_lst = []

        cur_left_ind = 0

        for i in range(0, len(A)):
            if A[i] == '0':
                count += 1
            else:
                count -= 1

            if count > max_count:
                max_count = count
                left_ind = cur_left_ind
                right_ind = i

            if count < 0:
                cur_left_ind = i + 1
                count = 0

        if left_ind == -1 and right_ind == -1:
            fnl_lst = []
        else:
            fnl_lst.append(left_ind + 1)
            fnl_lst.append(right_ind + 1)

        return fnl_lst


if __name__ == '__main__':
    s = Solution
    lst = '010'
    print(s.flip(lst))
