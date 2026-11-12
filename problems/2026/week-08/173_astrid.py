# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.iter = TreeNode(val=-1)
        self.inord = deque()

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            self.inord.append(node)
            dfs(node.right)
        dfs(root)


    def next(self) -> int:
        if self.inord:
            self.iter = self.inord.popleft()
        return self.iter.val

    def hasNext(self) -> bool:
        if self.inord:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()