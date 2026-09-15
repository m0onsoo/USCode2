class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # constraints:
        # what if matrix is empty? (m=n=0) what are the size of m and n?
        # is 0 integer or string?

        # solution:
        # start from (0, 0) and then iterate by row
        # when elem equals 0, set its entire row and column to 0's.
        # 0 만나면 sm, sn += 1, begin from sm, sn
        

        m, n = len(matrix), len(matrix[0])
        row, col = set(), set()
        
        # I takes O(mn) to iterate the matrix 
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        
        # print(row, col)
        
        # Below 2 loops take O(m+n)
        for r in row:
            for c in range(n):
                matrix[r][c] = 0
        
        for c in col:
            for r in range(m):
                matrix[r][c] = 0