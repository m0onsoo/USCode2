# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res = 0
        path = []
        def dfs(node):
            nonlocal res
            if not node:
                return 

            path.append(node.val)
            if not node.left and not node.right:
                res += int("".join(map(str, path))) 
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        dfs(root)
        return res