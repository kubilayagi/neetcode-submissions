# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(5)
        prev, cur = root, None
        if val < root.val:
            cur = root.left
        else:
            cur = root.right

        while cur:
            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if val < prev.val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

        return root