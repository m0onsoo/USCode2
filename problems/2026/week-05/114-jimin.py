# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        while cur:
            if cur.left:
                if cur.right:
                    stack.append(cur.right)
                cur.right = cur.left
                cur.left = None
            elif not cur.right and stack:
                cur.right = stack.pop()
            cur = cur.right