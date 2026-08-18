class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        mins = [0] * n

        for i in range(1, n):
            maxleft[i] = max(height[i-1], maxleft[i-1])

        for i in range(n - 2, -1, -1):
            maxright[i] = max(height[i+1], maxright[i+1])

        for i in range(n):
            trapped = min(maxleft[i], maxright[i]) - height[i]
            water += trapped if trapped >= 0 else 0       

        return water

            