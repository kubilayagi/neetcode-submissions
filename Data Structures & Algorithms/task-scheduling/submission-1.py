class MaxHeapNode:
    def __init__(self, count):
        self.count = count
        self.nextAvailable = 1

    def __lt__(self, other):
        # reversing this because we want a max heap instead of minheap
        return self.count > other.count

    def __repr__(self):
        return '(count:' + str(self.count) + ',nextAvail:' + str(self.nextAvailable) + ')'

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxFreq = 0
        freqs = {}
        h = []
        heapq.heapify(h)
        for t in tasks:
            freqs[t] = 1 + freqs.get(t, 0)
            maxFreq = max(maxFreq, freqs[t])
        
        for c in freqs.values():
            i = MaxHeapNode(c)
            heapq.heappush(h, i)

        q = deque()
        time = 0
        while h or q:
            time += 1
            # print(h)
            # print(q)
            # print('----')

            if h:
                task = heapq.heappop(h)
                task.count -= 1
                if task.count > 0:
                    task.nextAvailable = time + n
                    q.append(task)

            if q and q[0].nextAvailable == time:
                addBack = q.popleft()
                heapq.heappush(h, addBack)

        return time


    def leastIntervalGreedy(self, tasks: List[str], n: int) -> int:
        # adding this here for extra practice because there's
        # another way to do this with a greedy algorithm
        return 0