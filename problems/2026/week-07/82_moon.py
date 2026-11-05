# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        HEAD = prev = ListNode(val = 101, next = head)
        node = head
        
        while node:
            if node.next and node.val == node.next.val:
                # if there are duplicates
                while node.next and node.val == node.next.val:
                    node = node.next
                prev.next = node.next
            else:
                prev = node

            node = node.next
        
        return HEAD.next

      