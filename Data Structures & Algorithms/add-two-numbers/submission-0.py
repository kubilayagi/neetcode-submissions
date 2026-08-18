# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        resprev = dummy
        # handle normal adding case
        while l1 and l2:
            node = ListNode()
            nodesum = l1.val + l2.val + carry
            remainder = nodesum % 10
            if nodesum > 9:
                carry = 1
            else:
                carry = 0
            node.val = remainder
            resprev.next = node
            resprev = resprev.next
            l1 = l1.next
            l2 = l2.next

        remaininglist = None
        if l2 == None:
            remaininglist = l1
        elif l1 == None:
            remaininglist = l2
        # handle cases for when one list cuts off
        if carry == 0: # case when there is no carry value (easy)
            resprev.next = remaininglist
        else: # case when there is still a carry value (harder)
            if remaininglist == None:
                resprev.next = ListNode(1)
            else:
                while remaininglist:
                    nodesum = remaininglist.val + carry
                    remainder = nodesum % 10
                    if nodesum > 9:
                        carry = 1
                    else:
                        carry = 0
                    node = ListNode()
                    node.val = remainder
                    resprev.next = node
                    resprev = resprev.next
                    remaininglist = remaininglist.next
        
        if carry == 1:
            resprev.next = ListNode(1)

        return dummy.next