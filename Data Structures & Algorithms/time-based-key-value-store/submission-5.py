class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        vals = self.timeMap[key]
        if timestamp < vals[0][0]:
            return ""
        print(vals)
        # find the first timestamp that is less than the one we are passed
        l, r = 0, len(vals) - 1
        res = ""
        while l <= r:
            m = (r + l) // 2
            if vals[m][0] <= timestamp:
                l = m + 1
                # keep track of this progressively and return the last one until we
                # exit out of the loop, because that one will be the closest
                res = vals[m][1]
            else:
                r = m - 1
        return res