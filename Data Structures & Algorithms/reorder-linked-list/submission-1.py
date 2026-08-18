# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        temp = head
        while temp != None:
            count += 1
            temp = temp.next
            
        half = -1
        if count % 2 == 1:
            half = math.ceil(count / 2) - 1
        else:
            half = (count / 2)

        list1, list2 = head, head
        i = half
        while i > 1:
            list2 = list2.next
            i -= 1
        
        # list2 now points to the one right before the half
        # here, we cut off the end of what is list1, and then move list2 to point to the second half

        temp = list2.next
        list2.next = None
        list2 = temp

        # now reverse list2
        cur = list2
        prev = None
        while cur != None:
            tempnext = cur.next
            cur.next = prev
            prev = cur
            cur = tempnext
        list2 = prev

        # now we combine the two lists, the order int is used to determine whether we 
        # add from list1 or list2
        dummy = ListNode()
        order = 1
        cur = dummy
        while list1 and list2:
            if order > 0:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
            order *= -1

        if list1 == None:
            cur.next = list2
        elif list2 == None:
            cur.next = list1
        return

