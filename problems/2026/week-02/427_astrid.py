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
# Time complexity: n^2logn (level of nodes * maximum iteration for each level)
# Space complexity: n^2

from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # divide and conquer
        # use dfs to iterate sub grids recursively
        def dfs(n, r, c):
            isSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        isSame = False
                        # remember to left loop
                        break
                if not isSame:
                    break

            # turn the same grid into a leaf node
            if isSame:
                return Node(grid[r][c], True)

            # break into sub grids
            n = n // 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c+n)
            bottomleft = dfs(n, r+n, c)
            bottomright = dfs(n, r+n, c+n)
            return Node(1, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)
