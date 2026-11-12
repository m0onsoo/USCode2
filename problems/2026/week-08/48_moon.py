class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        n = 3
        (0,0) -> (0,2)
        (0,1) -> (1,2)
        (2,0) -> (0,0)

        c -> r
        """

        n = len(matrix)

        # (i, j) -> (j, n - 1 - i)
        # y = x

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        for i in range(n):
            matrix[i].reverse()

        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         matrix[i][j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[i][j]
        
        return matrix
