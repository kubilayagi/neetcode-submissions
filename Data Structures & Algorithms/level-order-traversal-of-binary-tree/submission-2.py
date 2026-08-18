# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = collections.defaultdict(list)
        def lot(node, level):
            nonlocal res
            if not node:
                return
            levels[level].append(node.val)
            lot(node.left, level + 1)
            lot(node.right, level + 1)
            return

        lot(root, 0)
        res = []
        for i in range(len(levels)):
            res.append(levels[i])
        return res