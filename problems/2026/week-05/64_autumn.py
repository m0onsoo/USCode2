class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) 
        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = grid[0][0] # base case

        # the first row arrives only from the cell on the left
        for col in range(1, cols): 
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        # the first col arrives only from the cell above
        for row in range(1, rows):  
            dp[row][0] = dp[row - 1][0] + grid[row][0] 

        # visit remaining rows & cols
        for row in range(1, rows):  
            for col in range(1, cols): 
                above = dp[row - 1][col] # get the min sum from the cell above
                left = dp[row][col - 1]  # get the min sum from the left cell
                dp[row][col] = min(above, left) + grid[row][col]

        return dp[rows - 1][cols - 1]  # the min sum is the very bottom-right cell