# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        fast = head.next
        slow = head
        while fast:
            if slow == fast:
                return True
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next

        return False
