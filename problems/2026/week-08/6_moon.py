class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1:
            return s
        
        zigzags = [[] for _ in range(numRows)]
        direction = 1

        r = 0
        for i, char in enumerate(s):
            # r = i % numRows
            if r == numRows - 1:
                direction = -1
            if r == 0:
                direction = 1


            zigzags[r].append(char)

            r += direction
        
        # print(zigzags)

        return ''.join([''.join(zig) for zig in zigzags])