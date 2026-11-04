# time complexity: O(n)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        cnt = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                k += 1
                nums[k-1] = nums[i]
        return k