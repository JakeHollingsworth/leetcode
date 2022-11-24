'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        for i, row in enumerate(grid):
            for j, square in enumerate(row):
                if square:
                    if i == 0:
                        total += 1
                    else:
                        total += 1 - grid[i-1][j]
                    if i == len(grid)-1:
                        total += 1
                    else:
                        total += 1 - grid[i+1][j]
                    if j == 0:
                        total += 1
                    else:
                        total += 1 - row[j-1]
                    if j == len(row) - 1:
                        total += 1
                    else:
                        total += 1 - row[j+1] 
        return total
