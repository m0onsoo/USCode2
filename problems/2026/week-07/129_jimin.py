# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        ans = 0
        if not root:
            return ans
        def dfs(node, path):
            nonlocal ans
            if not node.left and not node.right:
                ans += int(''.join(map(str,path))) # equal to ''.join([str(x) for x in path])
                return
            if node.left:
                path.append(node.left.val)
                dfs(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, path)
                path.pop()
        dfs(root, [root.val])
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        ans = 0
        if not root:
            return ans
        def dfs(node, path):
            nonlocal ans
            if not node.left and not node.right:
                ans += int(''.join(map(str,path))) # equal to ''.join([str(x) for x in path])
                return
            if node.left:
                path.append(node.left.val)
                dfs(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, path)
                path.pop()
        dfs(root, [root.val])
        return ans
