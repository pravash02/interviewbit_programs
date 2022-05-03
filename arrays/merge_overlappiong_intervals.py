from pandas._libs.interval import Interval


class Solution:
    @staticmethod
    def merge_ovrlp(A):
        new_interval = []
        i = 0
        A.sort(key=lambda x: x[0])
        new_interval.append(A[0])

        while i < len(A) - 1:
            if new_interval[i - 1][-1] == A[i + 1][0]:
                new_interval[i - 1][-1] = A[i + 1][-1]

            elif new_interval[i - 1][-1] > A[i + 1][0]:
                new_interval[i - 1][-1] = A[i + 1][-1]

            else:
                new_interval.append(A[i + 1])

            i += 1
        return new_interval

    @staticmethod
    def merge_ovrlp2(intervals):
        if (len(intervals) == 0):
            return intervals

        intervals.sort(key=lambda x: x.start)

        m = Interval(intervals[0].start, intervals[0].end)

        res = []
        i = 1

        while (i < len(intervals)):

            if (m.end >= intervals[i].start):
                m.end = max(m.end, intervals[i].end)
                i += 1

            else:
                res.append(m)
                m = Interval(intervals[i].start, intervals[i].end)
                i += 1

        res.append(m)
        return res


if __name__ == '__main__':
    s = Solution
    lst = [[1, 3], [2, 4], [5, 7], [6, 8]]
    lst2 = [[1, 3], [3, 5], [4, 6]]
    lst3 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(s.merge_ovrlp(lst2))
