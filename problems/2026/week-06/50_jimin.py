# https://leetcode.com/problems/powx-n/
import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x, n)
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n > 0:
            while n:
                ans = ans * x
                n -= 1
        elif n < 0:
            ans = 1
            while n:
                ans = ans / x
                n += 1
        return ans
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == -1:
            return 1/x
        q, r = n // 2, n % 2 # -1, 1
        half = self.myPow(x, q) # very important 
        if r:
            return x * half * half
        else:
            return half * half

    def myPow(self, x: float, n: int) -> float:
        def pow_pos(n):
            if n == 0:
                return 1
            half = pow_pos(n // 2)
            return x * half * half if n % 2 else half * half

        result = pow_pos(abs(n))
        return 1 / result if n < 0 else result