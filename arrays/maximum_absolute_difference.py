class Solution:

    @ staticmethod
    def max_arr(A):
        ap = []
        am = []
        for i in range(len(A)):
            ap.append(A[i] + i)
            am.append(A[i] - i)
        m1, m2 = (min(ap), max(ap))
        m3, m4 = (min(am), max(am))

        return max(abs(m1 - m2), abs(m3 - m4))

    # Brute Force Method
    @staticmethod
    def max_arr2(A):
        max_diff = 0

        for i in range(len(A)):
            for j in range(i, len(A)):
                curr_diff = abs(A[i]-A[j]) + abs(i+j)

                if curr_diff > max_diff:
                    max_diff = curr_diff

        return max_diff


if __name__ == '__main__':
    s = Solution
    lst = [-163, -5, 2, 4, 6, 8]
    print(s.max_arr(lst))
    # print(s.max_arr2(lst))
