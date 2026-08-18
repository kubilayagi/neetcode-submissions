# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node) -> bool:
            if not node:
                return False
            if not node.left and not node.right:
                return True
            leftleaf = dfs(node.left)
            rightleaf = dfs(node.right)
            
            if leftleaf and node.left.val == target:
                node.left = None
            if rightleaf and node.right.val == target:
                node.right = None

            if not node.left and not node.right:
                return True

            return False

        rootleaf = dfs(root) and root.val == target

        return None if rootleaf else root