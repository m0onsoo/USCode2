# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

        def find(inorder, postorder):
            if not inorder or not postorder:
                return None
                
            root_val = postorder[-1]
            node = TreeNode(root_val)
            postorder.pop() # O(1)

            for i, val in enumerate(inorder):
                if val == root_val:
                    node.right = find(inorder[i+1:], postorder)
                    node.left = find(inorder[:i], postorder)
            
            return node
        
        root = find(inorder, postorder)
        return root
