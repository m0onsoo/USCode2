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
        # devide and conquer

        def DC(rows, cols):
            sr, er = rows[0], rows[1]
            sc, ec = cols[0], cols[1]

            if (sr + 1 == er and sc + 1 == ec): # is leaf
                leaf = Node(val = grid[sr][sc], # mean T/F (1/0)
                            isLeaf = True,
                            topLeft = None,
                            topRight = None,
                            bottomLeft = None,
                            bottomRight = None)                            

                return leaf
            

            nr, nc = (sr + er) // 2, (sc + ec) // 2

            node = Node(val = grid[sr][sc], # mean T/F (1/0)
                        isLeaf = False,
                        topLeft = DC((sr, nr), (sc, nc)),
                        topRight = DC((sr, nr), (nc, ec)),
                        bottomLeft = DC((nr, er), (sc, nc)),
                        bottomRight = DC((nr, er), (nc, ec)))  

            if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf and node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                node.val = grid[sr][sc]
                node.isLeaf = True
                node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None

            return node

        n = len(grid)
        root = DC((0, n), (0, n))
        return root