'''
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  
'''
class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2:
            return n*'a'
        return (n-1) * 'a' + 'b'
