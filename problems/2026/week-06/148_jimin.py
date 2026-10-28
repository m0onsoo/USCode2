# https://leetcode.com/problems/sort-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        heap = []
        i = 0
        while head:
            heapq.heappush(heap, (head.val, i,  head))
            head = head.next
            i += 1

        dummy = ListNode()
        if not heap:
            return None
        _, _, cur = heapq.heappop(heap)
        dummy.next = cur
        while heap:
            _, _, cur.next = heapq.heappop(heap)
            cur = cur.next
        cur.next = None
        return dummy.next