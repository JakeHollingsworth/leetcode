'''
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
'''
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([p for p in patterns if p in word])
