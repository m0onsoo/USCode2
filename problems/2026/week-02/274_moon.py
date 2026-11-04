class Solution:
    def hIndex(self, citations: list[int]) -> int:
        num_papers = len(citations)

        # O(nlogn)
        citations.sort() # in-place

        # O(n)
        for i in range(1, num_papers + 1):
            if citations[i] >= num_papers - i:
                return num_papers - i

        return 0

        """
        # Brute Force
        # O(n^2)

        h_idx = 0
        num_papers = len(citations)

        for h in range(1, num_papers + 1):
            cnt = 0
            for citation in citations:
                if citation >= h:
                    # cited at least h times
                    cnt += 1
            
            if cnt >= h:
                # at least h papers
                h_idx = max(h_idx, h)

        return h_idx
        """

        
        # what if citations is empty == no paper -> h index = 0 ?