'''
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
'''
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sums = [sum(row) for row in mat]
        count = 0
        col_sums =[sum([row[j] for row in mat]) for j in range(len(mat[0]))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row_sums[row] == 1 and col_sums[col] == 1 and mat[row][col]:
                    count += 1
        return count
