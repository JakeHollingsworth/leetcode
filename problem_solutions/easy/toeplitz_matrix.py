'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) > len(matrix[0]):
            matrix = list(zip(*matrix)) # Transpose
        toeplitz = True
        n = len(matrix)
        m = len(matrix[0])
        for i in range(len(matrix) + len(matrix[0]) - 1):
            row = max(n - i - 1, 0)
            col = max(i - n + 1, 0)
            j = 0
            while row + j < n and col + j < m:
                toeplitz &= (matrix[row][col] == matrix[row+j][col+j])
                j += 1
        return toeplitz
        
