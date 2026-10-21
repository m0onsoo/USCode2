class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle) # number of rows
        dp = [] 

        for row in triangle:
            dp.append([0] * len(row))  # create a table

        dp[0][0] = triangle[0][0] 

        for row in range(1, n):  
            # calculate the min sum for each position
            for col in range(len(triangle[row])): 
                value = triangle[row][col]

                if col == 0:
                    dp[row][col] = dp[row - 1][col] + value
                elif col == len(triangle[row]) - 1:
                    dp[row][col] = dp[row - 1][col - 1] + value 
                else: 
                    above = dp[row - 1][col]  # get the min sum from the top position
                    upper_left = dp[row - 1][col - 1]  # get the min sum from the upper-left position
                    dp[row][col] = min(above, upper_left) + value  # choose the smallest sum

        return min(dp[-1])  # the smallest path sum is in the last row