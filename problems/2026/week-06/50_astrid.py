class Solution:
    def myPow(self, x: float, n: int) -> float:
        # turn it into binary representation
        isNeg = n < 0
        if n < 0:
            n = -n


        ans = 1.0
        while n > 0:
            if n & 1:
                # if lowest bit is 1, then multiply into the ans
                ans *= x           
            x *= x
            # remove the lowest bit
            n >>= 1
        
        return 1/ans if isNeg else ans
            



        # Cannot pass extreme test cases:
        # # turn it into binary representation
        # if n == 0:
        #     return 1
        # if n < 0:
        #     n = -n
        #     x = 1/x 

        # ans = 1
        # while n > 0:
        #     if n & 1:
        #         # if lowest bit is 1, then multiply into the ans
        #         ans *= x           
        #     x *= x
        #     # remove the lowest bit
        #     n >>= 1
        # return ans