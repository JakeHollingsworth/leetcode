'''
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_a, min_b = m, n
        for a,b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        return min_a * min_b
