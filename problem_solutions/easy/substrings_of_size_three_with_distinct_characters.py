'''
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.
'''
class Solution:
    def countGoodSubstrings(self, s: str, substr_len=3) -> int:
        if len(s) < substr_len:
            return 0
        res = 0
        for i in range(len(s) - substr_len + 1):
            chars = [c for c in s[i:i+substr_len]]
            if len(set(chars)) == len(chars):
                res += 1
        return res
