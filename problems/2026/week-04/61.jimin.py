# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # 0 <= k <= 2 * 109
        if not head:
            return head
            
        # connect the list
        dummy = ListNode()
        dummy.next = head
        count = 0
        prev = dummy
        while head:
            count += 1
            prev = prev.next
            head = head.next
        prev.next = dummy.next

        # calculate how much to push
        push = count - k % count

        # cut the loop
        cur = dummy.next
        prev = dummy
        for _ in range(push):
            cur = cur.next
            prev = prev.next
        

        prev.next = None

        return cur
