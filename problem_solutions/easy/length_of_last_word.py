'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    '''
    Simple test of python string manipulation.
    '''
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(s.split(' ')[-1])
