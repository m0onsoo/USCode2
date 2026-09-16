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
        root = prev = Node(0)
        while node:
            if node not in hashmap:
                # create corresponding node
                node_cpy = Node(node.val)
                hashmap[node] = node_cpy

            # connect next
            curr = hashmap[node]
            prev.next = curr
            prev = curr

            # connect random
            if node.random and hashmap.get(node.random):
                # None이 아니고 랜덤노드 해시맵 연결도 되어있으면
                rand = hashmap[node.random]

                curr.random = rand
            elif node.random:
                # 랜덤 노드 존재하는 경우 새로만들어주기
                rand = Node(node.random.val)
                hashmap[node.random] = rand

                curr.random = rand
            else:
                # 원본 노드 랜덤이 None이면
                curr.random = None

            # iterate
            node = node.next

        
        return root.next


            