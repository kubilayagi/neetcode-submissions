class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        minheap = []
        heapq.heappush(minheap, (0, k))
        visited = set()
        maxtime = 0

        while minheap:
            w1, n1 = heapq.heappop(minheap) # weight is the time to get to node
            if n1 in visited:
                continue
            visited.add(n1)
            maxtime = max(maxtime, w1)
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, (w1 + w2, n2))

        return maxtime if len(visited) == n else -1
