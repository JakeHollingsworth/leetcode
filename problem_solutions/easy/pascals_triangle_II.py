'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
        
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        row_fact = math.factorial(rowIndex)
        sol = [1]
        running_fact = row_fact / rowIndex
        base_fact = 1
        for i in range(1, rowIndex):
            sol.append(round(row_fact / (running_fact * base_fact)))
            running_fact /= (rowIndex-i)
            base_fact *= (i+1)
        return sol + [1]
