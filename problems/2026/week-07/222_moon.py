# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        """
        Line 13-22: The implementation uses a level-order traversal (BFS) which visits every node, resulting in a worst-case runtime of Θ(n).
        """
        
        if not root:
            return 0
        
        queue = deque([root])
        cnt = 0
        while queue:
            node = queue.popleft()
            cnt += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return cnt
