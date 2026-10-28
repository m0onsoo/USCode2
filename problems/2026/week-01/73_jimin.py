# https://leetcode.com/problems/set-matrix-zeroes/
# 처음 스캔할때 찾아내고
# 두 번째 스캔할때는 펑션 이용해서 채우기?

# 1차  : 타임리밋
# 2차 : 공간아웃 (Line 21: The 'visited' set and 'zeros' list can grow to O(m*n) size in the worst case, violating the O(m+n) auxiliary space limit.)
# 3차 : 여전히 zeros가 공간아웃. added_rows, added_cols 추가함


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        rows, cols = len(matrix), len(matrix[0])

        added_row = [False] * rows
        added_col = [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 and not(added_row[i] == True and added_col[j] == True):
                    zeros.append((i,j))
                    added_row[i] = True
                    added_col[j] = True


        check_row = [False] * rows
        check_col = [False] * cols

        def fill(r,c,d):
            matrix[r][c] = 0
            if c < cols-1 and d == 'r':
                fill(r,c+1, 'r')
            if 0 < c and d == 'l':
                fill(r,c-1, 'l')
            if r < rows-1 and d == 'd':
                fill(r+1,c, 'd')
            if 0 < r and d == 'u':
                fill(r-1,c, 'u')

        for r, c in zeros:
            if check_row[r] == False:
                fill(r,c,'r')
                fill(r,c,'l')
            if check_col[c] == False:
                fill(r,c,'u')
                fill(r,c,'d')

            
# 2차
        # visited = set()
        # def fill(r,c,d):
        #     if (r,c,d) in visited:
        #         return
        #     matrix[r][c] = 0
        #     if c < cols-1 and d == 'r':
        #         fill(r,c+1, 'r')
        #     if 0 < c and d == 'l':
        #         fill(r,c-1, 'l')
        #     if r < rows-1 and d == 'd':
        #         fill(r+1,c, 'd')
        #     if 0 < r and d == 'u':
        #         fill(r-1,c, 'u')
        #     visited.add((r,c,d))
        # for r, c in zeros:
        #     for d in ['r', 'l', 'd', 'u']:
        #         fill(r,c,d)
        #         visited.add((r,c,d))

        # 1차
        # def fill(r,c):
        #     for i in range(rows):
        #         for j in range(cols):
        #             if r == i:
        #                 matrix[i][j] = 0
        #             if c == j:
        #                 matrix[i][j] = 0
        # for r, c in zeros:
        #     fill(r,c)

                        