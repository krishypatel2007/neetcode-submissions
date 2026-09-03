class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # is new interval < curr interval?
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # is new interval after curr interval?
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # new interval is inbetween curr interval:
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        # our new interval is meant to be at the end
        res.append(newInterval)
        return res


            