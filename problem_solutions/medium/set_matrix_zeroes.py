'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def set_row_to_0(matrix, row):
            for i in range(len(matrix[0])):
                matrix[row][i] = (0 if matrix[row][i] is not None else None)

        def set_col_to_0(matrix, col):
            for i in range(len(matrix)):
                matrix[i][col] = (0 if matrix[i][col] is not None else None)

        # Set all 0s to None
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not matrix[row][col]:
                    matrix[row][col] = None
        
        # Look for Nones in matrix, set all non-None entries in row + col to 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] is None:
                    set_row_to_0(matrix, row)
                    set_col_to_0(matrix, col)

        # Reset None to 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] is None:
                    matrix[row][col] = 0
