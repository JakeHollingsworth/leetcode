'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

from typing import List

class Solution:
    '''
    This can be done with a simple loop over strs, checking for equality of all chars at the ith position. O(m*N), where
    N is the length of strs and m is the length of the shortest word in strs.
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        if len(strs) == 0: return ""
        for i, char in enumerate(strs[0]):
            for s in strs:
                if i == len(s) or s[i] != char: 
                    return longest_prefix
            longest_prefix += char
        return longest_prefix
