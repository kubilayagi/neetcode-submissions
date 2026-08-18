"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodemap = {} # maps original node => new node copy
        resdummy = Node(-1)
        headcur = head
        resprev = resdummy

        # build map of randompointer => 

        # first create the node list
        # along the way, keep track of which nodes are in which index
        while headcur != None:
            node = Node(headcur.val)
            resprev.next = node
            nodemap[headcur] = node
            resprev = node
            headcur = headcur.next

        # now attach all the random pointers
        headcur = head
        rescur = resdummy.next
        while headcur != None:
            if headcur.random == None:
                rescur.random = None
            else:
                rescur.random = nodemap[headcur.random]
            rescur = rescur.next
            headcur = headcur.next

        return resdummy.next