# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # root = last elem of postorder
        if len(inorder) == 0:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val, None, None)
        rootidx = inorder.index(root_val)
        in_left, in_right = inorder[:rootidx], inorder[rootidx+1:]
        post_left, post_right = postorder[:len(in_left)], postorder[len(in_left):-1]
        
        root.left = self.buildTree(in_left, post_left)
        root.right = self.buildTree(in_right, post_right)

        return root