# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def buildPath(node):
            res = []
            cur = root
            while cur and cur.val != node.val:
                res.append(cur)
                if node.val < cur.val:
                    cur = cur.left
                else:
                    cur = cur.right

            res.append(node)
            return res

        ppath = buildPath(p)
        qpath = buildPath(q)

        i = 0
        while i < min(len(ppath), len(qpath)) and ppath[i].val == qpath[i].val:
            i += 1

        return ppath[i-1]
            