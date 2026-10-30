class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        start, end = newInterval[0], newInterval[1]
        ind = 0
        while ind < n and start > intervals[ind][1]:
            res.append(intervals[ind])
            ind += 1
        while ind < n and end >= intervals[ind][0]:
            start = min(start, intervals[ind][0])
            end = max(end, intervals[ind][1])
            ind += 1
        res.append([start, end])

        while ind < n:
            res.append(intervals[ind])
            ind += 1
        return res