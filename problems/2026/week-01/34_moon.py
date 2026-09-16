class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def BinarySearch(left, right):
            if left > right:
                # end condition
                return -1

            mid = (left + right) // 2
            if nums[mid] == target:
                # happy path
                return mid
            
            if nums[mid] < target:
                return BinarySearch(mid + 1, right)
            else:
                return BinarySearch(left, mid - 1)
        
        # return the index of the target number if it exists, else return -1
        left = right = BinarySearch(0, len(nums) - 1)

        L, R = left, right
        while left > 0 and nums[left - 1] == nums[left]:
            # find the left boundary in O(logn)
            left = BinarySearch(0, left - 1)
            if left != -1:
                L = left
        while 0 <= right < len(nums) - 1 and nums[right] == nums[right + 1]:
            # find the right boundary in O(logn)
            right = BinarySearch(right + 1, len(nums) - 1)
            if right != -1:
                R = right

        return [L, R]