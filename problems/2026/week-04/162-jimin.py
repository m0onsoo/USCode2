# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        peak = 0
        n = len(nums)
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                peak = i

        
        if n > 1 and nums[0] > nums[1]:
            peak = 0
        if n > 1 and nums[n-1] > nums[n-2]:
            peak = n-1

        return peak
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        n = len(nums)

        if n == 0:
            return None
        elif n == 1:
            return 0

        while l <= r:
            mid = (l+r) // 2

            if mid == 0 and nums[0] > nums[1]:
                return 0
            elif mid == n-1 and nums[n-1] > nums[n-2]:
                return n-1
            elif nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1