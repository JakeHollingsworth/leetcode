'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n = format(n, "b")
        return n[0] == "1" and n.count("1") == 1
