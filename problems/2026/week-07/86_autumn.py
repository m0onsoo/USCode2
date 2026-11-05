# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # temp starting nodes
        small = ListNode(0) # nodes < x
        large = ListNode(0) # nodes >= x

        # track the last node
        small_tail = small   
        large_tail = large
        current = head

        while current is not None: 
            next_node = current.next 
            current.next = None  # detach the current node from the original list

            if current.val < x: 
                small_tail.next = current  
                small_tail = current  # update the last node
            else:
                large_tail.next = current 
                large_tail = current  # update the last node

            current = next_node 

        small_tail.next = large.next  # connect the smaller group and the larger group
        
        return small.next  # we do not need a temp node