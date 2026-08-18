class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x + 1
        while l < r:
            m1 = ((r - l) // 2) + l #floor
            m2 = m1 + 1 #ceil
            m1sq = m1 ** 2
            m2sq = m2 ** 2
            if x >= m1sq and x <= m2sq:
                return m2 if x == m2sq else m1
            elif x >= m2sq:
                l = m2
            else:
                r = m1
        return -1
