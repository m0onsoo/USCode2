"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    # space complexity: O(1)
    def connect(self, root: 'Node') -> 'Node':        
        # iterator for the current layer
        cur = root

        while cur:
            dummy = Node(0)
            # iterator for the next layer
            tail = dummy

            # build up the next layer linked list
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next

            # update to the head of next layer
            cur = dummy.next

        return root



    # space complexity: O(n)       
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        dq = deque()
        dq.append(root)

        while dq:
            level = len(dq)
            for i in range(level):
                node = dq.popleft()
                if i < level - 1:
                    node.next = dq[0]
                
                # append next layer
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root            
                
        