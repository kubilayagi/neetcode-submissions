# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
 
        prev = None
        cur = root

        while cur and cur.val != key:
            prev = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right

        if not cur:
            return root
        elif not cur.left and not cur.right:
            if not prev:
                return None
            if prev.left == cur:
                prev.left = None
            elif prev.right == cur:
                prev.right = None
        elif cur.left and cur.right:
            delnode = cur
            rparent = None # right subtree parent
            cur = cur.right
            while cur.left:
                rparent = cur
                cur = cur.left
            if rparent:
                rparent.left = cur.right
                cur.right = delnode.right

            cur.left = delnode.left

            if not prev:
                return cur
            if prev.left == delnode:
                prev.left = cur
            elif prev.right == delnode:
                prev.right = cur
        else:
            child = cur.left if cur.left else cur.right
            if not prev:
                return child
            if prev.left == cur:
                prev.left = child
            elif prev.right == cur:
                prev.right = child

        return root