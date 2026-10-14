# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # create a hashmap
        inorder_index = {}
        for index, value in enumerate(inorder):
            inorder_index[value] = index

        # the final postorder value is the root
        postorder_index = len(postorder) - 1

        def build(inorderL, inorderR):
            nonlocal postorder_index

            # if inorder is empty, the tree is also empty
            if inorderL > inorderR:
                return None

            root_value = postorder[postorder_index]
            postorder_index -= 1
            root = TreeNode(root_value)
            root_index = inorder_index[root_value]

            root.right = build(root_index + 1, inorderR)
            root.left = build(inorderL, root_index - 1)

            return root

        return build(0, len(inorder) - 1)    