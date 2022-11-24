'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return rows
        else:
            for i in range(2, numRows):
                rows += [[1]+[rows[-1][i] + rows[-1][i+1] for i in range(len(rows[-1])-1)]+[1]]
        return rows        
            
