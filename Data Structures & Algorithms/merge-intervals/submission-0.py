class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        res = []
        l, r = intervals[0][0], intervals[0][1]
        for i in intervals[1:]:
            nl, nr = i[0], i[1]
            if nl > r: # next interval, add prev one to res and move on
                res.append([l, r])
                l = nl
                r = nr
            elif nr > r:
                r = nr

        res.append([l, r])

        return res