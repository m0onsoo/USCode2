# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        
        node = head
        pref_head = prefix = ListNode()
        suf_head = suffix = ListNode()
        # prefix -> suffix

        while node:
            if node.val < x:
                prefix.next = node
                node, prefix = node.next, node
            else:
                suffix.next = node
                node, suffix = node.next, node
        
        suffix.next = None
        prefix.next = suf_head.next
        return pref_head.next
                


        