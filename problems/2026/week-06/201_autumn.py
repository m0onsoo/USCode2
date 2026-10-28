class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0 # a counter for the num of bits that has been removed

        while left != right:
            # remove the rightmost bits
            left = left >> 1 
            right = right >> 1 
            count += 1 # track the number of bit position removed

        return left << count # recover the removed bits with 0