# https://leetcode.com/problems/construct-quad-tree/?envType=study-plan-v2&envId=top-interview-150

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
        root = Node()
        length = len(grid)

        def dq(rs, cs, n):
            if n == 0:
                return Node(grid[rs][cs], True, None, None, None, None)
            n = n//2
            tl = dq(rs, cs, n)
            tr = dq(rs, cs+n, n)
            bl = dq(rs+n, cs, n)
            br = dq(rs+n, cs+n, n)

            # br = dq(matrix[rs+n:][cs+n:], rs+n, cs+n, n)

            if tl.val == tr.val == bl.val == br.val:
                if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
                    return Node(tl.val, True, None, None, None, None)
                else:
                    return Node(tl.val, False, tl, tr, bl, br)
            else:
                return Node(tl.val, False, tl, tr, bl, br) # set isLeaf False to indicate it has leaves

        return dq(0, 0, length)

        # while n > 1:
            
        #     n = n // 2

        # return root

    def construct(self, grid: List[List[int]]) -> 'Node':
        root = Node()
        length = len(grid)

        def dq(matrix, n):
            if n == 1:
                return Node(matrix[0][0], True, None, None, None, None)
            n = n//2
            tl = dq([row[0:n] for row in matrix[0:n]], n)
            tr = dq([row[n:] for row in matrix[0:n]], n)
            bl = dq([row[0:n] for row in matrix[n:]], n)
            br = dq([row[n:] for row in matrix[n:]], n)

            # br = dq(matrix[rs+n:][cs+n:], rs+n, cs+n, n)

            if tl.val == tr.val == bl.val == br.val:
                if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
                    return Node(tl.val, True, None, None, None, None)
                else:
                    return Node(tl.val, False, tl, tr, bl, br)
            else:
                    return Node(1, False, tl, tr, bl, br)

        return dq(grid, length)