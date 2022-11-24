'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = - mat[len(mat)//2][len(mat)//2] if len(mat) % 2 else 0
        for i in range(len(mat)):
            total += mat[i][i] + mat[len(mat) - 1 - i][i]
        return total
