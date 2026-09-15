class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy solution :)

        overlaps = 0
        intervals.sort(key = lambda pair : pair[1])
        lastEnd = intervals[0][1]

        # iterate through sorted intervals
        for start, end in intervals[1:]:
            # is there an overlap?
            if start < lastEnd:
                overlaps += 1
            else:
                lastEnd = end

        return overlaps
        