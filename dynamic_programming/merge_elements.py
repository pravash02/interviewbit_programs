class Solution:

    def solve(self, A):
        pass
        # # Check for wrong input
        # if new_interval.start > new_interval.end:
        #     new_interval.start, new_interval.end = new_interval.end, new_interval.start
        #
        # output = []
        #
        # newStart = new_interval.start
        # newEnd = new_interval.end
        #
        # i = 0
        #
        # # As long as we dont find the newInterval insert position, we add the existing elements
        # while i < len(intervals) and newStart > intervals[i].end:
        #     output.append(intervals[i])
        #     i += 1
        #
        # # Now we have the insert position.
        # # As long as we can merge, make a newStart as minimum Value and newEnd as maximum Value, so as to accomodate as many intervals possible
        # while i < len(intervals) and newEnd >= intervals[i].start:
        #     newStart = min(newStart, intervals[i].start)
        #     newEnd = max(newEnd, intervals[i].end)
        #     i += 1
        #
        # # Now we have merged intervals
        # output.append(Interval(newStart, newEnd))
        #
        # # If there are any leftovers in original Intervals which we cannot merge, add them to output
        # while i < len(intervals):
        #     output.append(intervals[i])
        #     i += 1
        #
        # return output


if __name__ == '__main__':
    s = Solution()
    A = [1, 3, 7]
    print(s.solve(A))
