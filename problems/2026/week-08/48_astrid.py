class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 2 3
        # 4 5 6
        # 7 8 9

        # 7 8 9
        # 4 5 6
        # 1 2 3

        # 7 4 1
        # 8 5 2
        # 9 6 3

        # flip it by diagnols
        for i in range(len(matrix)):
            for j in range(i+1, (len(matrix[0]))):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # firstly flip it by column
        for i in range(len(matrix)):
            matrix[i].reverse()
        