class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones] # negative for max heap
        heapq.heapify(h)
        while len(h) > 1:
            one = heapq.heappop(h)
            two = heapq.heappop(h)
            if one != two:
                heapq.heappush(h, one - two)
        return 0 if len(h) == 0 else -1 * heapq.heappop(h) # multiply again by -1 because max heap