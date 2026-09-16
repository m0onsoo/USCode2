class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])

        first_column_zero = False

        # create markers using the first row/column
        for row in range(rows):
            if matrix[row][0] == 0:
                first_column_zero = True

            for column in range(1, columns):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0

        # zero cells excluding the marker
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0

        # the first row
        if matrix[0][0] == 0:
            for column in range(columns):
                matrix[0][column] = 0

        # the first column
        if first_column_zero:
            for row in range(rows):
                matrix[row][0] = 0