# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        # DFS
        # when hit the leaf, add to the sum

        total = 0
        stack = [(root, "")]

        while stack:
            node, curr_path = stack.pop()
            curr_path += str(node.val)
            if not node.left and not node.right:
                # leaf node
                total += int(curr_path)
            
            if node.left:
                stack.append((node.left, curr_path))
            if node.right:
                stack.append((node.right, curr_path))
        
        return total