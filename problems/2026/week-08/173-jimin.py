# https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: TreeNode | None):
        self.dummy = TreeNode()
        self.pointer = self.dummy
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.pointer.right = TreeNode(node.val, None, None)
            self.pointer = self.pointer.right
            dfs(node.right)
        dfs(root)

    def next(self) -> int:
        self.dummy = self.dummy.right
        return self.dummy.val

    def hasNext(self) -> bool:
        return True if self.dummy.right else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()