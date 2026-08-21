class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        path = []
        subTreeSize = {}
        maxSubtree = 0

        def dfs(node):
            nonlocal subTreeSize
            nonlocal maxSubtree
            if node in path:
                return (False, -1)
            if node in visited:
                return (True, 1 + len(path))
            subtreeSize = 1
            for nbr in adj[node]:
                if path and nbr == path[-1]:
                    continue
                path.append(node)
                subres = dfs(nbr)
                if not subres[0]:
                    return (False, -1)
                subtreeSize += subres[1]
                path.pop()

            subTreeSize[node] = subTreeSize
            visited.add(node)

            return (True, subtreeSize)

        for i in range(n):
            res = dfs(i)
            if not res[0]:
                return False
            maxSubtree = max(maxSubtree, res[1])

        return maxSubtree == n
