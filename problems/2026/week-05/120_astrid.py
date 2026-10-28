# using dp
# dp[r][i] the minimun path sum at current row r index i
# dp[r][i] = min(dp[r-1][i], dp[r-1][i-1])
# base case: at row 0, dp[0][i] = triangle[0][i]
# we want: the total minimun path sum: iterate through the last row to get the global minimum

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        
        # create dp array
        dp = [[0] * len(row) for row in triangle]
        dp[0][0] = triangle[0][0]
        
        for r in range(1, n):
            for i in range(len(dp[r])):
                if i == 0:
                    dp[r][i] = dp[r-1][i] + triangle[r][i]
                elif i >= len(dp[r-1]):
                    dp[r][i] = dp[r-1][i-1] + triangle[r][i]
                else:
                    dp[r][i] = min(dp[r-1][i], dp[r-1][i-1]) + triangle[r][i]
        
        # iterate through the last level
        return min(dp[n-1])




    # optimized  
    def minimumTotal2(self, triangle: list[list[int]]) -> int:
            # bottom up
            dp = triangle[-1][:]
            for r in range(len(triangle)-2, -1, -1):
                for i in range(len(triangle[r])):
                    dp[i] = min(dp[i], dp[i+1]) + triangle[r][i]
    
            return dp[0]