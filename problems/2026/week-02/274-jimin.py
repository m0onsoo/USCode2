# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
        
    def hIndex(self, citations: list[int]) -> int:
        citations.sort() # 0 1 3 5  / 1 1 3
        n = len(citations)

        if n == 1:
            return 1 if citations[0] else 0
        if max(citations) == 0:
            return 0
        
        # search the rightmost index + 1 of 0
        index = bisect.bisect_right(citations, 0)
        citations = citations[index:]

        l, r = 0, len(citations) - 1 
        ans = 1

        while l <= r:
            mid = (l + r) // 2
            if citations[mid] <= r - mid + 1:
                ans = max(ans, citations[mid])
                l = mid + 1
            else:
                r = mid - 1

        if len(citations) < citations[0]:
            return max(ans, len(citations))
        return ans

    def hIndex(self, citations: list[int]) -> int:
        
        citations.sort() # 0 1 3 5  / 1 1 3
        prev = 0
        ans = 0
        n = len(citations)
        for i, c in enumerate(citations):
            for j in range(prev, c+1):
                if j < n - i + 1:
                    ans = max(j, ans)
            prev = c

        return ans