class TimeMap:

    def __init__(self):
        # key => [(timestamp, value)]
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        vals = self.store[key]
        l, r = 0, len(vals) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m - 1

        return res

        
