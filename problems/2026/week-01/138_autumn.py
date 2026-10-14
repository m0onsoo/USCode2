"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        originals = []
        copies = []

        current = head
        while current:
            originals.append(current)
            copies.append(Node(current.val))
            current = current.next

        n = len(copies)

        # connect next pointers
        for i in range(n - 1):
            copies[i].next = copies[i + 1]

        # connect random pointers
        for i in range(n):
            random_node = originals[i].random

            if random_node is None:
                copies[i].random = None
            else:
                for j in range(n):
                    if originals[j] is random_node:
                        copies[i].random = copies[j]
                        break

        return copies[0]