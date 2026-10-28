# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity: o(n)
# space complexity: o(n)


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # use postorder to determine the root
        # then use the root to get left and right tree
        idx_map = {val: i for i, val in enumerate(inorder)}
        def dfs(instart, inend, poststart, postend):
            if instart >= inend:
                return None

            rootval = postorder[postend - 1]
            root = TreeNode(rootval)

            inrootidx = idx_map[rootval]
            leftlen = inrootidx - instart
            leftpostend = poststart + leftlen

            root.left = dfs(instart, inrootidx, poststart, leftpostend)
            root.right = dfs(inrootidx+1, inend, leftpostend, postend-1)
            
            return root

        return dfs(0, len(inorder), 0, len(postorder))