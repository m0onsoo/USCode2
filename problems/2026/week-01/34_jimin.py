# 48분.. 엣지케이스 노가다 너무 함
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# 1차 생각: 그냥 일일히 보면 안되나? -> 숫자가 너무 많은가 (O(n) 이면 안되는건가)
# Line 13: The implementation uses a linear scan (for loop) over the array, resulting in O(n) time complexity.

# 2차생각 : binary search
# recursive 하게 호출해야하려나 like divide and conquer

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        ans = []
        left, right = None, None

        if len(nums) == 1 and target == nums[0]:
            return [0,0]

        def dq(l, r):
            nonlocal left
            nonlocal right

            if l > r or left and right:
                return

            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0: #left
                    left = 0
                if mid == len(nums)-1:
                    right = len(nums)-1
                if 0 < mid and nums[mid-1] != target:
                    left = mid
                if mid < len(nums) - 1 and nums[mid+1] != target:
                    right = mid
                if not left:
                    dq(l, mid-1)
                if not right:
                    dq(mid+1, r)
            elif nums[mid] < target:
                dq(mid+1, r)
            else:
                dq(l, mid-1)

        dq(0, len(nums)-1)
        ans = [left, right]

        return [-1, -1] if left is None and right is None else ans
        # not 은 0이랑 None 구별 못함

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if not nums:
    #         return [-1, -1]
        
    #     prev = nums[0]
    #     ans = []
    #     first_found = False
    #     for i, num in enumerate(nums):
    #         if num == target:
    #             if not first_found:
    #                 ans.append(i)
    #                 first_found = True
    #         if first_found and num != target:
    #             ans.append(i-1)
    #             break
    #     return ans if ans else [-1, -1]