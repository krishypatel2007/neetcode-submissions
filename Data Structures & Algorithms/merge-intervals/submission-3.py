class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort list by start value
        intervals.sort(key = lambda pair: pair[0])
        res = [intervals[0]]

        for start, end in intervals:
            last = res[-1][1] # end of the last apppended interval
            #check for overlap
            if last >= start:
                # we have an overlap
                res[-1][1] = max(last, end)
            else:
                res.append([start,end])
        return res


            

        
        