# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []

        # pre-order = DFS: O(N)
        stack = [root]
        queue = deque()
        while stack:
            node = stack.pop()  # traverse in pre-order
            queue.append(node)  # store in pre-order
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        # traverse and connect: O(N)
        prev, prev.left = queue.popleft(), None  # root
        while queue:
            node = queue.popleft()
            prev.right, prev, prev.left = node, node, None



            