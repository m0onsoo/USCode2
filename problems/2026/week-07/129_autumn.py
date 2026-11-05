# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node, root_to_leaf):  # Return the sum of completed path numbers in this subtree.
            # base case
            if node is None: 
                return 0

            root_to_leaf = root_to_leaf * 10 + node.val  # apply a higher digit

            # the node is a leaf
            if node.left is None and node.right is None:  
                return root_to_leaf 

            left_sum = dfs(node.left, root_to_leaf)  
            right_sum = dfs(node.right, root_to_leaf)  

            return left_sum + right_sum 

        return dfs(root, 0) 