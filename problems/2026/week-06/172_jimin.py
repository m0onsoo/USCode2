
# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # need to count how many 2 and 5s
        # might need to memo or dp or recursive..
        # only need to count 5s
        ans = 0
        while n:
            ans += n // 5
            n = n // 5
        return ans