################################################################################
# Question:

# 56. Merge Intervals - Medium


# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

################################################################################


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x:(x.start,x.end))
        r = [intervals[0]]
        for c in intervals[1:]:
            if r[-1].end >= c.start:
                p = r.pop(-1)
                r.append(Interval(p.start, max(c.end, p.end)))
            else:
                r.append(c)
        return r
        