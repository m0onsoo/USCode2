# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode()
        node = ListNode()

        temp = ListNode()
        temp_head = temp

        first_node_found = False
        while head:
            if head.val < x:
                node.next = ListNode(head.val)
                if not first_node_found:
                    dummy.next = node.next
                    first_node_found = True
                node = node.next
            else:
                temp.next = ListNode(head.val)
                temp = temp.next
            head = head.next
        
        head = dummy
        while head.next:
            head = head.next
        head.next = temp_head.next

        return dummy.next


    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small, big = ListNode(), ListNode()
        s, b = small, big

        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                b.next = head
                b = b.next
            head = head.next

        b.next = None          # cut the big side
        s.next = big.next      # attatch small - big
        return small.next