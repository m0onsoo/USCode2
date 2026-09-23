import sys
class Solution:
    def jump(self, nums: list[int]) -> int:
        # dp[i] = min num of jumps to reach ith index
        n = len(nums)
        dp = [sys.maxsize] * n
        dp[0] = 0

        # O(nK) ~ O(n^2) / n: nums, K: max steps
        for i, num in enumerate(nums):
            for step in range(1, num + 1):
                if i + step < n:
                    dp[i + step] = min(dp[i + step], dp[i] + 1) 
        
        return dp[n - 1]

        