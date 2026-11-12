# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        # pointer should be initialized to a non-existent number smaller than any element in the BST
        
        # find the most left node and then connect with initial pointer
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Moves the pointer to the right, then returns the number at the pointer
        # next action is always valid == stack never empty when they call
        
        curr = self.stack.pop()

        if curr.right:
            node = curr.right
            while node:
                self.stack.append(node)
                node = node.left
        
        return curr.val


    def hasNext(self) -> bool:
        # Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false

        return True if len(self.stack) > 0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()