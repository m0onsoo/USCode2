# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # base case
        if head is None or head.next is None:  
            return head

        # split the given linked list into two
        slow = head 
        fast = head.next  

        while fast is not None and fast.next is not None:
            slow = slow.next  # move forward by one node
            fast = fast.next.next  # move forward by two nodes

        # save the second half of the given linked list
        second_head = slow.next
        slow.next = None  # disconnect the first and the second half

        # sort two lists recursively
        left = self.sortList(head)
        right = self.sortList(second_head) 

        dummy = ListNode(0)  # track the first node of the result
        tail = dummy  # track the last node of the result

        # merge the lists
        while left is not None and right is not None:
            if left.val <= right.val:
                tail.next = left # add the smaller node
                left = left.next # move to the next node since the first one is selected
            else:
                tail.next = right # add the smaller node
                right = right.next # move to the next node since the first one is selected
            tail = tail.next # points the new last node

        # if either left or right is empty
        if left is not None: # right list is empty
            tail.next = left  # add all remaining nodes
        else: # left list is empty
            tail.next = right  # add any remaining nodes

        return dummy.next  # this is the real first node