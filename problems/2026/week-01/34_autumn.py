class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_boundary(find_first: bool) -> int:
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                middle = left + (right - left) // 2

                if nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    # middle should be valid
                    answer = middle

                    if find_first:
                        # earlier occurrence
                        right = middle - 1
                    else:
                        # later occurrence
                        left = middle + 1

            return answer

        first = find_boundary(True)

        if first == -1:
            return [-1, -1]

        last = find_boundary(False)

        return [first, last]