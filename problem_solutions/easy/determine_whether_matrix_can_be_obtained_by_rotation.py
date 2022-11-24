'''
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            print(mat)
            if mat == target:
                return True
            else:
                mat = [list(col[::-1]) for col in zip(*mat)]
        return False
