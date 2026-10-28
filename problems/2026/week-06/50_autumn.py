class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if x == 0:
            return 0.0
        elif n == 0:
            return 1.0

        negative = n < 0  # remember whether n was negative
        n = abs(n)  # use a nonnegative exponent

        # initialization
        result = 1.0  
        curr_product = x 

        # bitwise exponentiation
        while n > 0:
            # if n is odd
            if n % 2 == 1:
                result *= curr_product

            curr_product *= curr_product # square the current power
            n //= 2 # move to the right bit

        if negative:  # check whether the original n was negative
            return 1.0 / result  # compute the reciprocal only after exponentiation
        return result

    # # This solution gives a wrong answer to a certain example cuz it computes the neg n first and it results in a small rounding error.
    # def myPow(self, x: float, n: int) -> float:
    #     # base cases
    #     if x == 0:
    #         return 0.0
    #     elif n == 0:
    #         return 1.0
        
    #     # handle negative n
    #     if n < 0:
    #         x = 1 / x
    #         n = -n

    #     # initialization
    #     result = 1.0
    #     curr_product = x

    #     # bitwise exponentiation
    #     while n > 0:
    #         # if n is odd
    #         if n % 2 == 1:
    #             result *= curr_product

    #         curr_product *= curr_product
    #         n //= 2 # move to the right bit

    #     return result


        