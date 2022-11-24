'''
A square matrix is said to be an X-Matrix if both of the following conditions hold:

All the elements in the diagonals of the matrix are non-zero.
All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.
'''
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        return all( (grid[i][j] != 0) if (i==j or i == (len(grid)-j-1)) else not grid[i][j]  for i in range(len(grid)) for j in range(len(grid)))
