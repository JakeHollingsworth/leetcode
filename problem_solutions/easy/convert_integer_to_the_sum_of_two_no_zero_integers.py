'''
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions you can return any of them.
'''
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for n1 in range(n//2,n):
            n2 = n - n1
            if '0' not in str(n1) and '0' not in str(n2):
                return [n1, n2]
        return None
