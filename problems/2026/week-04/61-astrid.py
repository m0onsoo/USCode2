# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head
        # get length and tail node
        p = dummy
        n = 0
        rend = ListNode()
        while p.next:
            n += 1
            p = p.next
        rend = p

        if k % n == 0:
            return head

        steps = n - k % n
        prev, cur = dummy, dummy.next
        for _ in range(steps-1):
            cur = cur.next
            prev = prev.next
        # now reaching the cutting point
        rsta = cur.next
        cur.next = None
        # connect to head
        rend.next = dummy.next
        dummy.next = rsta

        return dummy.next



        



    # brute force: Time exceeded O(kN)
    # def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
    #     if not head:
    #         return None

    #     dummy = ListNode()
    #     dummy.next = head
    #     end = ListNode()
    #     for _ in range(k):
    #         prev = dummy
    #         cur = dummy.next
    #         while cur.next:
    #             cur = cur.next
    #             prev = prev.next
    #         end = cur
    #         # cut in the tail
    #         prev.next = None
    #         # connect to the head
    #         end.next = dummy.next
    #         dummy.next = end
    #     return dummy.next
