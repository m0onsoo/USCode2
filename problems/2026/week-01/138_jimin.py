# https://leetcode.com/problems/copy-list-with-random-pointer/
# 53분 걸림 ㅜㅜ
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 1차실패 : Random pointer of node with label 13 points to a node from the original list.
# 일단 랜덤 생성 하면서 dict에 담고 두번째 돌면서 연결하는거 어때?

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0) # 여기에 값을 꼭 넣어줘야 하는 이유?
        random_corr = {}
        if not head:
            return None

        prev = Node(head.val, head.next, head.random)
        random_corr[head] = prev
        dummy.next = prev


        # Traverse and copy (Simple)
        while head.next:
            new = Node(head.next.val, head.next.next, head.next.random)

            random_corr[head.next] = new
            head = head.next
            prev.next = new
            prev = new

        cur = dummy.next
        while cur:
            if cur.random:
                cur.random = random_corr[cur.random]
            cur = cur.next

        return dummy.next