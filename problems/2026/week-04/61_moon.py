# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        # 1. edge case
        if not head:
            return None
        
        # 2. construct a cycle
        # time: O(n), memory: O(1)
        prev, node = None, head
        n = 0
        while node:
            prev, node = node, node.next
            n += 1
        prev.next = head

        # 3. find a new head
        # time: O(n), memory: O(1)
        tail, new_head = None, head
        for _ in range(n - k % n):
            tail = new_head
            new_head = new_head.next
        tail.next = None # cut the cycle

        return new_head

