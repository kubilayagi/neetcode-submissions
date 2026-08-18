class MedianFinder:

    def __init__(self):
        self.first = [] # maxheap for first, smaller half of numbers
        self.second = [] # min heap for second, bigger half of numbers

    def addNum(self, num: int) -> None:
        if self.second and num > self.second[0]:
            heapq.heappush(self.second, num)
        else:
            heapq.heappush_max(self.first, num)
        
        if len(self.first) > len(self.second) + 1:
            top = heapq.heappop_max(self.first)
            heapq.heappush(self.second, top)
        if len(self.second) > len(self.first) + 1:
            top = heapq.heappop(self.second)
            heapq.heappush_max(self.first, top)


    def findMedian(self) -> float:
        if len(self.first) == len(self.second):
            return (self.first[0] + self.second[0]) / 2
        elif len(self.first) > len(self.second):
            return self.first[0]
        else:
            return self.second[0]
        
        