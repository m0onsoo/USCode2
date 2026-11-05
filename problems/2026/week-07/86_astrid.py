# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        lessdum = ListNode()
        greatdum = ListNode()

        if not head:
            return None

        p = head
        curless = ListNode()
        curless = lessdum
        curgreat = ListNode()
        curgreat = greatdum
        while p:
            if p.val < x:
                curless.next = p
                curless = curless.next
            else:
                curgreat.next = p
                curgreat = curgreat.next
            p = p.next
        
        # MLE， need to cut the list
        curgreat.next = None
        # connect less part with greater part
        curless.next = greatdum.next

        return lessdum.next