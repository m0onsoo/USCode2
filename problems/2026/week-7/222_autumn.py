# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        # base case
        if root is None:  
            return 0 

        left_height = 0  # start with the left tree
        current = root  

        # DFS
        while current is not None:
            left_height += 1  
            current = current.left 

        right_height = 0
        current = root

        # DFS
        while current is not None:  
            right_height += 1 
            current = current.right  

        # a tree is perfect
        if left_height == right_height: 
            return 2 ** left_height - 1 

        left_count = self.countNodes(root.left) 
        right_count = self.countNodes(root.right)

        # a tree is not perfrect
        return 1 + left_count + right_count