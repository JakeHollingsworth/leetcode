'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {(0,0): grid[0][0]}
        def minSum(i, j):
            if (i, j) not in memo:
                memo[(i,j)] = grid[i][j] + min(minSum(i - 1, j) if i-1>=0 else float('inf'), minSum(i, j-1) if j-1>=0 else float('inf')) 
            return memo[(i, j)]
        return minSum(len(grid)-1, len(grid[0]) - 1)
