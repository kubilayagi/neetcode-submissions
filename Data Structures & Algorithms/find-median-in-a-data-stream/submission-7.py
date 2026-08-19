class MedianFinder:

    def __init__(self):
        self.left = [] # maxheap for smaller numbers
        self.right = [] # minheap for bigger numbers
        

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush_max(self.left, num)

        if len(self.left) > len(self.right) + 1:
            val = heapq.heappop_max(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush_max(self.left, val)
           
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return self.left[0]
        else:
            return self.right[0]
        
        