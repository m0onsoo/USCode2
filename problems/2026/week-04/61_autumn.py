# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # if the input is Null
        if head is None or head.next is None or k == 0:  
            return head

        # initialization
        length = 1 
        tail = head 

        # check the length of the given list
        while tail.next is not None: 
            tail = tail.next 
            length += 1

        # the full rotation changes nothing
        k = k % length
        if k == 0: 
            return head 

        # initialization for the new list
        new_tail = head
        
        # split at the node just before the new head
        for _ in range(length - k - 1):  
            new_tail = new_tail.next 

        new_head = new_tail.next 
        new_tail.next = None 
        tail.next = head  # connect the second chunk to the original head

        return new_head
        