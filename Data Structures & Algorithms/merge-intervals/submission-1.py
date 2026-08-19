class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l, r = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            il = intervals[i][0]
            ir = intervals[i][1]
            if il >= l and ir <= r:
                continue
            elif il <= r:
                r = ir
            elif il > r:
                res.append([l, r])
                l = il
                r = ir

        res.append([l, r])

        return res