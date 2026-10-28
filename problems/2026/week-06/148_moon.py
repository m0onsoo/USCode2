# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        
        arr = []

        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        arr.sort()


        new_head = prev = ListNode()
        for num in arr:
            node = ListNode(val = num)
            prev.next, prev = node, node
        
        return new_head.next
        
        # is set muttable?