#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = []

        for num1 in nums1:
            for num2 in nums2:
                pair_sum = num1 + num2
                heap.append((pair_sum, num1, num2))

        heapq.heapify(heap)

        ans = []

        for i in range(k):
            pair_sum, num1, num2 = heapq.heappop(heap)
            ans.append([num1, num2])

        return ans

    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        
        i, j = 0, 0
        ans = []
        heap = []
        heapq.heappush(heap, (nums1[i]+nums2[j], i, j))
        seen = set()
        seen.add((0,0))
        for _ in range(k):
        #     ans.append([nums1[i], nums2[j]])
        #     if nums1[i + 1] + nums2[j] < nums1[i] + nums2[j]:
        #         i += 1
        #     else:
        #         j += 1
        # return ans
            _, idx1, idx2 = heapq.heappop(heap)

            ans.append([nums1[idx1], nums2[idx2]])
            i, j = idx1, idx2
            if i < len(nums1)-1 and (i+1, j) not in seen:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                seen.add((i+1, j))
            if j < len(nums2)-1 and (i, j+1) not in seen:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                seen.add((i, j+1))

        return ans