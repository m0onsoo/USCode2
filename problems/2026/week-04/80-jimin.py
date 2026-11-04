# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        l = 0
        prev = None
        for num in nums:
            if num == prev:
                count += 1
            else:
                prev = num
                count = 1
            if count <= 2:
                nums[l] = num
                l += 1
        return l


    # def removeDuplicates(self, nums: list[int]) -> int:
    #     l = 0
    #     for num in nums:
    #         if l < 2 or num != nums[l - 2]:
    #             nums[l] = num
    #             l += 1
    #     return l