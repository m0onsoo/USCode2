"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        hashmap = {} # key = original node, val = copied node

        node = head
        while node:
            # construct hashmap
            node_cpy = Node(node.val)
            hashmap[node] = node_cpy

            node = node.next
        
        node = head
        root = prev = Node(0)
        while node:
            # connect next
            curr = hashmap[node]
            prev.next = curr
            prev = curr

            # connect random
            rand = hashmap[node.random] if node.random else None
            curr.random = rand

            node = node.next
        
        return root.next


            