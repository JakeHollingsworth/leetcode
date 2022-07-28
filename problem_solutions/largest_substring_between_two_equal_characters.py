'''
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.
'''
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        for i, c in enumerate(s):
            if c not in first_occurrence:
                first_occurrence[c] = i
            last_occurrence[c] = i
        max_substr_len = -1
        for char, start in first_occurrence.items():
            end = last_occurrence[char]
            max_substr_len = max(max_substr_len, end - start - 1)
        return max_substr_len
