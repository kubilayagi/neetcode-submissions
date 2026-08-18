# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        res = []
        q.append([root, 0])
        while len(q) > 0:
            cur = q.popleft()
            level = cur[1]
            val = cur[0].val
            if len(res) - 1 < level:
                res.append([val])
            else:
                res[level].append(val)
            
            if cur[0].left:
                q.append([cur[0].left, level + 1])
            if cur[0].right:
                q.append([cur[0].right, level + 1])

        return res