class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0  
        right = len(nums) - 1

        while left < right:
            # starts from the middle item
            mid = (left + right) // 2 

            # halves the list
            if nums[mid] < nums[mid + 1]: # if the slope goes upward
                left = mid + 1  # the peak exists on the right, so get rid of the left side
            else:  # if the slope goes downward
                right = mid  # the peak exists on the left, so get rid of the right side

         # either left or right is the peak, since it is the only remaining item
        return left

        # return nums.index(max(nums)) # this gives O(n log n)