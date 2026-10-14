class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        
        for i, citation in enumerate(citations):
            # if pass, at least i+1 papers are cited i+1 times
            if citation < i + 1:
                return i
        
        # all citations exceed the number of papers 
        return len(citations)