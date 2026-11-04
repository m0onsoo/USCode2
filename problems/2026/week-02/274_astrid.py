# time complexity: o(nlogn)
# space complexity: o(n)


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # sort first, then iterate
        citations = sorted(citations, reverse=True)
        h = 0
        for i, ci in enumerate(citations):
            if ci < i + 1:
                if i > 0:
                    return min(i, citations[i-1])
                else:
                    return 0
        
        return len(citations)