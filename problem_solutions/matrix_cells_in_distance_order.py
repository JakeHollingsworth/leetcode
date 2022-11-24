'''
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
'''
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        current = [[rCenter, cCenter]]
        res = []
        visited = set()
        visited.add((rCenter, cCenter))
        while current:
            temp = []
            for i,j in current:
                res.append([i,j])
                if i > 0 and (i-1, j) not in visited:
                    visited.add((i-1, j))
                    temp.append([i-1, j])
                if i+1 < rows and (i+1, j) not in visited:
                    visited.add((i+1, j))
                    temp.append([i+1, j])
                if j > 0 and (i, j-1) not in visited:
                    visited.add((i, j-1))
                    temp.append([i, j-1])
                if j+1 < cols and (i, j+1) not in visited:
                    visited.add((i, j+1))
                    temp.append([i, j+1])                    
            current = temp
        return res

