class Solution:
    @staticmethod
    def merge_intervals(A, interval):
        if len(interval) <= 1:
            return interval

        i = 0
        while i < len(A):

            if interval[0] > A[i][-1]:
                i += 1
                continue
            elif interval[-1] < A[i][0]:
                A.insert(i, interval)
                break
            else:
                interval[0] = min(A[i][0], interval[0])
                interval[-1] = max(A[i][-1], interval[-1])
                del A[i]

        if i == len(A):
            A.append(interval)

        return A


if __name__ == '__main__':
    s = Solution
    lst = [[1, 3], [6, 10]]
    lst2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    interval = [2, 5]
    interval2 = [4, 9]
    print(s.merge_intervals(lst2, interval2))
