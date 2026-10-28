#  https://leetcode.com/problems/bitwise-and-of-numbers-range/
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        start = right
        # for i in range(left, right):
        #     start = start & i

        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1

        return left << i