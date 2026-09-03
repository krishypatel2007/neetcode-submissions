"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0,0
        s,e = 0,0
        while s < len(intervals):
            # do we have a new overlap?
            if start[s] < end[e]:
                count += 1
                s += 1
            else: # ie we reached an end/ edge case where both start/end are equal
                e += 1
                count -= 1
            res = max(res, count)
        return res



        