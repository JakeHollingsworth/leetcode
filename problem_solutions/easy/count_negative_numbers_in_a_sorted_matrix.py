'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = 0
        while i < len(grid) and grid[i][0] >= 0:
            i += 1
        negatives = (len(grid) - i) * (len(grid[0]) - 0)
        curr_row,curr_col = i,0
        for curr_row in range(curr_row-1, -1, -1):
            while curr_col < len(grid[0]) and grid[curr_row][curr_col] >= 0:
                curr_col += 1
            negatives += len(grid[0]) - curr_col
        return negatives # O(M+N)
