'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_delta = 1
        col_delta = 1
        horizontal_moving = True
        i,j = 0,-1
        ans = []
        for _ in range(len(matrix) * len(matrix[i])):
            if horizontal_moving:
                j += col_delta
            else:
                i += row_delta
            if not horizontal_moving and (i == len(matrix) or i == -1 or matrix[i][j] == 'x'):
                i -= row_delta
                j += col_delta
                row_delta *= -1
                horizontal_moving = True
            if horizontal_moving and (j == len(matrix[0]) or j == -1 or matrix[i][j] == 'x'):
                j -= col_delta
                i += row_delta
                col_delta *= -1
                horizontal_moving = False
            ans.append(matrix[i][j])
            matrix[i][j] = 'x'
        return ans

