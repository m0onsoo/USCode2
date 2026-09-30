class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []

        # collect all possible combinations
        for i in nums1:
            for j in nums2:
                pairs.append((i + j, i, j))

        pairs.sort()

        result = []

        for pair_sum, i, j in pairs[:k]:
            result.append([i, j])

        return result