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

    # organized one
    def deleteDuplicates2(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)

        prev = dummy
        cur = ListNode()

        while prev.next:
            cur = prev.next
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
                
        return dummy.next


        
            