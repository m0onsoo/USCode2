class Solution:
    # we need to find how many 10 we can make
    def trailingZeroes(self, n: int) -> int:
        factor_five = 0 # a counter for the number of factors of five
        divisor = 5 # start from 5k

        while divisor <= n:
            factor_five += n // divisor # count all possible factors of the divisor
            divisor *= 5 # move to the next power of 5

        return factor_five # this is the number of (2, 5) pairs
