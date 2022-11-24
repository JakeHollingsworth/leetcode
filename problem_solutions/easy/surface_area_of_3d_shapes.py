'''
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.
'''
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface_area = 0
        for i, row in enumerate(grid):
            for j, h in enumerate(grid[i]):
                surface_area += max(0, h - grid[i-1][j]) if i > 0 else h
                surface_area += max(0, h - grid[i+1][j]) if i < len(grid) - 1 else h
                surface_area += max(0, h - grid[i][j-1]) if j > 0 else h
                surface_area += max(0, h - grid[i][j+1]) if j < len(grid[i]) - 1 else h
                surface_area += 2 * (h != 0)
        return surface_area
