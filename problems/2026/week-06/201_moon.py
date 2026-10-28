class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
            
        res = 0
        for i in range(31, -1, -1):  # 32 bit
            l_bit = (left >> i) & 1
            r_bit = (right >> i) & 1

            if l_bit == r_bit:
                if l_bit == 1:
                    res += 2 ** i  # 누적해서 더해줌
            else:
                break
        
        return res
        
        # 2진수 -> 10진수 (010001)
        # 010001
        # 001101
        # 000001 and

        # 4 = 0100
        # 5 = 0101
        # 6 = 0110
        # 7 = 0111
        # 8 = 1000
        #     100

        # 0000 ~ 1111
        