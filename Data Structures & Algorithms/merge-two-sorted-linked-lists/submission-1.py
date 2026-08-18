# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        c1 = list1
        c2 = list2
        cur = dummy
        while c1 != None and c2 != None:
            if c1.val < c2.val:
                cur.next = c1
                c1 = c1.next
            else:
                cur.next = c2
                c2 = c2.next
            cur = cur.next

        cur.next = c1 if not c2 else c2
        return dummy.next
        