import heapq
from collections import deque

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

        heap = [] # min-heap

        # time: O(k log k)
        # memory: O(k)
        # (두 수의 합, nums1의 인덱스 i, nums2의 인덱스 j)로 통일
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        res = []

        # time: O(k log k)
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            # i번째 행에서 nums2의 다음 인덱스(j + 1)가 존재하면 push
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res


        """
        # Memory Limit Exceeded
        # memory: O(n^2)

        combs = []

        for n1 in nums1:
            for n2 in nums2:
                combs.append((n1 + n2, n1, n2))
        
        heapq.heapify(combs)
        
        res = []
        for _ in range(k):
            _, u, v = heapq.heappop(combs)
            res.append([u, v])
        
        return res
        """
