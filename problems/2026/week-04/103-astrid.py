# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []


        dq = deque()
        dq.append(root)
        nxtlen = 1
        res = []

        while dq:
            # reset level list for every level
            level = []
            curlen = nxtlen
            nxtlen = 0
            for _ in range(curlen):
                cur = dq.popleft()
                level.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                    nxtlen += 1
                if cur.right:
                    dq.append(cur.right)
                    nxtlen += 1
               
            if len(res) % 2 != 0:
                level = level[::-1]
            res.append(level)

        return res