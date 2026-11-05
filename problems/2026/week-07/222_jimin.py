
# https://leetcode.com/problems/count-complete-tree-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        # Interesting : at least one subtree is a complete binary tree
        if not root:
            return 0

        left_height = 0 
        node = root
        while node:
            node = node.left
            left_height += 1
        right_height = 0 
        node = root
        while node:
            node = node.right
            right_height += 1

        if  left_height == right_height:
            return 2 ** left_height - 1
        
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)