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
        # check whether the tree is empty
        if root is None:
            return 

        nodes = []  
        stack = [root] # store a reference to the root

        while stack:  # visit every node
            node = stack.pop() 
            nodes.append(node)

            # put the right child nodes because it is a pre-order, so the left child should be visited first
            if node.right is not None: 
                stack.append(node.right)
            if node.left is not None: 
                stack.append(node.left) 

        for i in range(len(nodes)):
            nodes[i].left = None  # remove the left child pointer because now it is a linked list
            if i + 1 < len(nodes): 
                nodes[i].right = nodes[i + 1] 
            else: 
                nodes[i].right = None 
        