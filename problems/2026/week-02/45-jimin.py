# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def jump(self, nums: list[int]) -> int:
        # DP ? out of idea..
        # Try BFS? -> Memory Limit Exceeded

        q = deque([(0, 0)])
        ans = float('inf')
        n = len(nums)

        if n == 1:
            return 0

        while q:
            cur, hops = q.popleft()
            jumps = nums[cur]
            for jump in range(1, jumps+1):
                if cur + jumps >= n - 1:
                    ans = min(ans, hops + 1)
                if cur + jumps < n-1:
                    q.append((cur + jump, hops + 1))
        return ans

    def jump(self, nums: list[int]) -> int:

        farthest = nums[0]
        ans = 0
        n = len(nums)
        if n == 1:
            return 0
        for i, num in enumerate(nums):
            for j in range(i, farthest):
                if j + num > farthest:
                    farthest = i + num
            ans += 1
            if i + num >= n-1:
                return ans
                
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        cur_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest

        return jumps
                
        
            
       
       
       
       
        # DP. 
        # dp[n] = min(dp[k] + 1) where 0 < k < n-1 and nums[k] >= n - k

        # dp = [0 for _ in range(len(nums))]
        # dp[0] = 0

        # for i, num in enumerate(nums):
        #     for k in range(num):