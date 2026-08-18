class HeapObject:
    def __init__(self, coords: List[int]):
        self.coords = coords

    def __repr__(self):
        return str(self.coords)

    def __lt__(self, other):
        owndist = math.sqrt(((self.coords[0] - 0) ** 2) + ((self.coords[1] - 0) ** 2))
        otherdist = math.sqrt(((other.coords[0] - 0) ** 2) + ((other.coords[1] - 0) ** 2))
        return owndist < otherdist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        for p in points:
            pobj = HeapObject(p)
            heapq.heappush(h, pobj)

        res = []
        for i in range(0, k):
            res.append(heapq.heappop(h).coords)

        return res