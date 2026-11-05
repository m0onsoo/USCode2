# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        # O(logn**2)
        # calculate height for left and right separately
        if not root:
            return 0

        def get_height(root):
            h = 0
            while root:
                h += 1
                root = root.left
            return h

        left_h = get_height(root.left)
        right_h = get_height(root.right)

        if left_h == right_h:
            # left tree is a full binary tree
            return 2**left_h - 1 + 1 + self.countNodes(root.right)
        elif left_h > right_h:
            # right tree is a full binary tree
            return 2**right_h - 1 + 1 + self.countNodes(root.left)


        
    def countNodes0(self, root: TreeNode | None) -> int:
        # brute force
        if not root:
            return 0

        # bfs
        stack = [root]
        ans = 1
        while stack:
            node = stack.pop()
            if node.left:
                ans += 1
                stack.append(node.left)
            if node.right:
                ans += 1
                stack.append(node.right)
        
        return ans

        