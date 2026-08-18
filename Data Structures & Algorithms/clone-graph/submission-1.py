"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # node => [neighbor nodes]
        adj = collections.defaultdict(list)
        val2node = {}
        q = deque()
        q.append(node)
        while q:
            n = q.popleft()
            if n in adj:
                continue
            clone = Node(n.val)
            val2node[n.val] = clone
            adj[n] = n.neighbors
            for nbr in n.neighbors:
                if nbr not in adj:
                    q.append(nbr)

        q.append(node)
        visited = set()
        while q:
            n = q.popleft()
            if n in visited:
                continue
            visited.add(n)
            clone = val2node[n.val]
            for nbr in n.neighbors:
                clone.neighbors.append(val2node[nbr.val])
                if nbr not in visited:
                    q.append(nbr)

        return val2node[node.val]

        
