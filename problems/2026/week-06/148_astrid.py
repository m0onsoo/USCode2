# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # using merge sort
        if not head or not head.next:
            return head
        
        # find the middle point and cut the linkedlist from there
        slow, fast = head, head.next
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        mid = slow.next
        slow.next = None

        # iteration
        left = self.sortList(head)
        right = self.sortList(mid)

        # sort the current sublist
        dummy = ListNode()
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        
        cur.next = left or right
        return dummy.next




        # # using divide and conquer
        # if not head:
        #     return None

        # # conquer:
        # # get pivot: head of the sublinkedlist
        # # move every node x with x.val < pivot.val to the left
        # def conquer(pivot, end):
        #     left = pivot
        #     right = ListNode()
        #     while left.next is not end:
        #         if left.val < pivot.val:
        #             # move to left
        #             right = left.next
        #             pivot.next = right.next
        #             right.next = dummy.next
        #             dummy.next = right
        #         left = left.next


        # dummy = ListNode()
        # dummy.next = head
        # pivot = head

        # left = pivot
        # right = ListNode()
        # while left.next:
        #     if left.val < pivot.val:
        #         # move to left
        #         right = left.next
        #         pivot.next = right.next
        #         right.next = dummy.next
        #         dummy.next = right
        #     left = left.next
        
        # # divide:
        # # left: [head, pivot]
        # # right: [pivot.next, end]
        # conquer(dummy.next, pivot)
        # conquer(pivot.next, None)



        

        


            

