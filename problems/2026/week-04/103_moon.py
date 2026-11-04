# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # 1. edge case
        if not root:
            return []

        # 2. solution
        # time: O(n)
        queue = deque([root])
        level = 0
        res = []
        while queue:          
            levels = []  
            for _ in range(len(queue)):
                curr = queue.popleft()
                levels.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            if level % 2 == 0:
                res.append(levels)
            else:
                # O(n)
                res.append(levels[::-1])
            
            level += 1



        return res
