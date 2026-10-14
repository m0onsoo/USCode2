# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check whether the tree is empty
        if root is None:  
            return [] 

        # initialization
        result = [] 
        curr_level = [root]
        left_to_right = True # since root considers as left to right direction

        # check all nodes in the current level
        while curr_level: 
            level_values = []  # all values of the current level
            next_level = []  # all nodes in the next level

            for node in curr_level: 
                level_values.append(node.val)
                if node.left is not None: 
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right) 

            # check whether the order should be reversed
            if not left_to_right: 
                level_values.reverse()

            # append it as a separate list
            result.append(level_values) 

            # update
            curr_level = next_level
            left_to_right = not left_to_right

        return result