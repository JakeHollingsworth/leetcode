'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def index_to_element(mat, ind):
            num_cols = len(matrix[0])
            row = ind // num_cols
            col = ind % num_cols
            return mat[row][col]
        
        def leftmost_binary_search(arr, targ):
            l = 0
            r = len(arr[0]) * len(arr)
            while l < r:
                m = (l + r) // 2
                if index_to_element(arr, m) < targ:
                    l = m+1
                else:
                    r = m
            return l
        
        index = leftmost_binary_search(matrix, target)
        return (index < (len(matrix) * len(matrix[0]))) and (index_to_element(matrix, index) == target)
