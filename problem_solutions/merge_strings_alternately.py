'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left_over = len(word1) - len(word2)
        res = ''.join([a + b for a,b in zip(word1, word2)])
        if left_over != 0:
            res += word2[left_over:] if left_over < 0 else word1[-left_over:]
        return res
