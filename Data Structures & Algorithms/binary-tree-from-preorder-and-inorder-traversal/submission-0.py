# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iomap = {} # value => position in list
        for i, n in enumerate(inorder):
            iomap[n] = i
        print(iomap)
        preorder.reverse()

        def dfs(left, right):
            nonlocal preorder
            if left >= right:
                return None
            
            val = preorder.pop()
            node = TreeNode()
            node.val = val
            node.left = dfs(left, iomap[val])
            node.right = dfs(iomap[val] + 1, right)
            return node

        return dfs(0, len(inorder))

            
