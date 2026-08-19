class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))

        visited = set()
        res = -1
        heap = []
        heapq.heappush(heap, (0, k))
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1
            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (w1 + w2, n2))

        return res if len(visited) == n else -1