class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][0]
        overlap = 0
        for times in intervals:
            start = times[0]
            if start < end:
                overlap += 1
            else:
                end = times[1]
        return overlap