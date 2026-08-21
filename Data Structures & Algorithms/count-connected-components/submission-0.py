class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        res = []
        visited = set()

        def bfs(node, parent):
            comp = set()
            q = deque()
            q.append((node, parent))

            while q:
                n1, p1 = q.popleft()
                if n1 in comp:
                    continue
                comp.add(n1)
                visited.add(n1)
                for n2 in adj[n1]:
                    if n2 != parent and n2 not in comp:
                        q.append((n2, n1))

            res.append(comp)

        for i in range(n):
            if i not in visited:
                bfs(i, -1)

        return len(res)