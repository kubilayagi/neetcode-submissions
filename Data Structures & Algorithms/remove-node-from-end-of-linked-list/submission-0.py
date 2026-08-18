# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cpoint = head
        while cpoint != None:
            count += 1
            cpoint = cpoint.next

        if count == n:
            return head.next

        onebefore = count - n
        i = 1
        cur = head
        while i < onebefore:
            cur = cur.next
            i += 1

        cur.next = cur.next.next

        return head

        