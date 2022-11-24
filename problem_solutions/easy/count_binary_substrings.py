'''
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        total = 0
        while i < len(s)-1:
            if s[i] != s[i+1]:
                left = i
                right = i + 1
                while left >= 0 and right < len(s) and s[left] == s[i] and s[right] == s[i+1]:
                    total += 1
                    left -= 1
                    right += 1
            i += 1
        return total
