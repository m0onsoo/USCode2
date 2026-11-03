#  https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        
        seen = set()
        dummy = ListNode()
        pointer = dummy

        cur = head
        while cur.next:
            if cur.val != cur.next.val and cur.val not in seen:
                pointer.next = cur
                pointer = pointer.next
            seen.add(cur.val)
            cur = cur.next
        if cur.val not in seen:
            pointer.next = cur
        else:
            pointer.next = None
        return dummy.next
            

    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        
        dummy = ListNode()
        pointer = dummy

        prev_val = -101
        cur = head
        while cur.next:
            if cur.val != cur.next.val and cur.val != prev_val:
                pointer.next = cur
                pointer = pointer.next
            prev_val = cur.val
            cur = cur.next
        if cur.val != prev_val:
            pointer.next = cur
        else:
            pointer.next = None
        return dummy.next
            

