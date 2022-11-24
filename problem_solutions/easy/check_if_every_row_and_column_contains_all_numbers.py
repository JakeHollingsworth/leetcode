'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
'''
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = [set(r) for r in matrix]
        cols = [set(c) for c in zip(*matrix)]
        return all(len(r) == len(matrix) for r in rows) and all(len(c) == len(matrix) for c in cols) 
