class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        # digkstra?

        m, n = len(grid), len(grid[0])

        # init
        dists = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        dists[0][0] = grid[0][0]

        for r in range(m):
            for c in range(n):
                # update minimum weight to the specific node
                if r - 1 >= 0:
                    dists[r][c] = min(dists[r - 1][c] + grid[r][c], dists[r][c])
                if c - 1 >= 0:
                    dists[r][c] = min(dists[r][c - 1] + grid[r][c], dists[r][c])
        
        return dists[m - 1][n - 1]