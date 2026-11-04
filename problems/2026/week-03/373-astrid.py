import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        # using heap
        # initialize: the smallest one is [0,0]
        candis = []
        heapq.heappush(candis, (nums1[0] + nums2[0], 0, 0))
        visited = set()
        visited.add((0,0))
        res = []

        # stop when getting k pairs, make sure the heap isn't empty
        target1, target2 = 0, 0
        m, n = len(nums1), len(nums2)
        while k and candis:
            tar, i, j = heapq.heappop(candis)
            res.append([nums1[i],nums2[j]])

            if i < m-1:
                if (i+1, j) not in visited:
                    heapq.heappush(candis, (nums1[i+1] + nums2[j], i+1, j))
                    visited.add((i+1, j))
            if j < n-1:
                if (i, j+1) not in visited:
                    heapq.heappush(candis, (nums1[i] + nums2[j+1], i, j+1))
                    visited.add((i, j+1))            
            k -= 1

        return res