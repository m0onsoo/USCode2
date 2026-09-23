"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def build(row, column, size):
            top_left_value = grid[row][column]
            is_equal = True

            for r in range(row, row + size):
                for c in range(column, column + size):
                    if grid[r][c] != top_left_value:
                        is_equal = False
                        break
                if not is_equal:
                    break

            # Base case (all 0s or 1s)
            if is_equal:
                return Node(bool(top_left_value), True, None, None, None, None)

            # Recursive case
            half = size // 2
            top_left = build(row, column, half)
            top_right = build(row, column + half, half)
            bottom_left = build(row + half, column, half)
            bottom_right = build(row + half, column + half, half)

            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        return build(0, 0, len(grid))
        