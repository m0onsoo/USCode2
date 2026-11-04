class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if not nums:
            return 
        
        # divide and conquer: O(N)
        def search_peak(left: int, right: int) -> int:
            if right - left <= 1:
                # O(1)
                return left if nums[left] > nums[right] else right

            
            mid = (left + right) // 2
            lmax_idx = search_peak(left, mid)
            rmax_idx = search_peak(mid, right)

            return lmax_idx if nums[lmax_idx] > nums[rmax_idx] else rmax_idx

        idx = search_peak(0, len(nums) - 1)
        
        return idx
