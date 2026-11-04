class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = sum(nums)
        # using kadane's algorithms
        cur_max = -float('inf')
        all_max = -float('inf')
        
        cur_min = float('inf')
        all_min = float('inf')
        for x in nums:
            cur_max = max(x, cur_max+x)
            all_max = max(cur_max, all_max)

            cur_min = min(x, cur_min+x)
            all_min = min(cur_min, all_min)
        
        # if all elements are less than 0
        if all_max < 0:
            return int(all_max)
        # the maximum would come from the original array or the ring array
        return int(max(all_max, total - all_min))
        
        

        

             