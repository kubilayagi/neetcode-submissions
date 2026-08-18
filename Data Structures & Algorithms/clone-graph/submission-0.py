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
        q = deque()
        m = {}
        q.append(node)
        while q:
            cur = q.popleft()
            if cur.val in m:
                continue
            m[cur.val] = Node(cur.val, [])
            for neighbor in cur.neighbors:
                q.append(neighbor)

        q.append(node)
        while q:
            cur = q.popleft()
            if len(m[cur.val].neighbors) > 0:
                continue
            for neighbor in cur.neighbors:
                m[cur.val].neighbors.append(m[neighbor.val])
                q.append(neighbor)

        return m[1]

        