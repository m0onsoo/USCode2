class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k, n = 0, len(nums)
        max_num = 3 * 10 ** 4 + 1
        # O(n)
        for i, num in enumerate(nums[:n - 2]):
            chk_idx = i + 2
            while chk_idx < n and num == nums[chk_idx]:
                # replace num into max number
                nums[chk_idx] = max_num

                k += 1
                chk_idx += 1
            i = chk_idx

        # O(nlogn)
        nums.sort()

        return n - k
