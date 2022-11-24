'''
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_inds = [row.index(min(row)) for row in matrix]
        result = []
        for i, ind in enumerate(min_inds):
            if matrix[i][ind] == max([matrix[j][ind] for j in range(len(matrix))]):
                result.append(matrix[i][ind])
        return result
