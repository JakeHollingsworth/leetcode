'''
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= (m*n)
        rows_shift = k // n
        cols_shift = (k % n)
        for _ in range(rows_shift):
            grid = [grid.pop(-1)] + grid
        for _ in range(cols_shift):
            curr_val = grid[0][0]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if j == n-1:
                        next_x, next_y = (i+1, 0) if i != m-1 else (0,0)
                    else:
                        next_x, next_y = i, j + 1
                    grid[next_x][next_y], curr_val = curr_val, grid[next_x][next_y]
        return grid
