class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        vol = 0
        while l < r:
            lh = heights[l]
            rh = heights[r]
            width = r - l
            vol = max(min(lh, rh) * width, vol)
            if lh > rh:
                r-=1
            else:
                l+=1
        return vol