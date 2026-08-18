# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def heightdfs(node):
            if not node:
                return 0
            return 1 + max(heightdfs(node.left), heightdfs(node.right))
        
        def dfs(node):
            nonlocal res
            if not node:
                return
            res = max(res, heightdfs(node.left) + heightdfs(node.right))
            dfs(node.left)
            dfs(node.right)
        
            
        dfs(root)
        return res