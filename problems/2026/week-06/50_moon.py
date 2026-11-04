class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n

        # TLE
        # res = 1
        # for _ in range(abs(n)):
        #     res *= x
        
        # if n >= 0:
        #     return res
        # return res if n >= 0 else 1 / res

        def DQ(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x
            
            half_n = n // 2
            half_pow = DQ(x, half_n) 

            return half_pow * half_pow if n % 2 == 0 else half_pow * half_pow * x
        res = DQ(x, abs(n))
        return res if n >= 0 else 1 / res