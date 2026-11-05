# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head

        while cur:
            if not cur.next:
                break
            elif cur.val != cur.next.val:
                cur = cur.next
                prev = prev.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # reconnect with the distinct elements
                prev.next = cur.next
                cur = cur.next
       
        return dummy.next

            