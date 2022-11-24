'''
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return 2*n if n%2 else n
