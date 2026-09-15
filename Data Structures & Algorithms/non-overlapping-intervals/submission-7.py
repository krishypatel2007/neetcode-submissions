class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlaps = 0
        intervals.sort(key = lambda pair : pair[0])
        res = [intervals[0]]

        # iterate through sorted intervals
        for start, end in intervals[1:]:
            lastEnd = res[-1][1] # our last end literally
            # is there an overlap?
            if start < lastEnd:
                overlaps += 1
                res[-1][1] = min(lastEnd, end)
            else:
                res.append([start,end])

        return overlaps
        