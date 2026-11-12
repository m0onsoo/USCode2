# O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # we only need to know which row each charactor located at
        buckets = ["" for _ in range(numRows)]
        curr = 0
        step = 1
        
        for ch in s:
            buckets[curr] += ch
            
            # update direction when reaching the end
            if curr == numRows - 1:
                step = -1
            elif curr == 0:
                step = 1
            # update the row of the next charactor
            curr = curr + step
        
        return "".join(buckets)
        
        

