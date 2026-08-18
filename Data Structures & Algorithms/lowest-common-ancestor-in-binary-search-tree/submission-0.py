# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ppath = self.buildPath(root, p)
        qpath = self.buildPath(root, q)

        i = 0
        lca = root
        while i < min(len(ppath), len(qpath)):
            if ppath[i].val == qpath[i].val:
                lca = ppath[i]
            else:
                break
            i += 1

        return lca
        

    def buildPath(self, root: TreeNode, n: TreeNode):
        res = []
        cur = root
        while cur and cur.val != n.val:
            res.append(cur)
            if n.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        res.append(n)
        print(res)
        return res