class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((w, v))
        
        q = []
        heapq.heappush(q, (0, src))
        res = collections.defaultdict(int)
        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in res:
                continue
            res[n1] = w1
            for w2, n2 in adj[n1]:
                if n2 not in res:
                    heapq.heappush(q, (w1 + w2, n2))

        for i in range(n):
            if i not in res:
                res[i] = -1

        return dict(res)
