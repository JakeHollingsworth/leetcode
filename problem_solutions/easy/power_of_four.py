'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 0:
            if n % 2:
                return n == 1
            n >>=1
            if n % 2:
                return False
            n >>= 1
        return False
