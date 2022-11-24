'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = {}
        for ch in s:
            if ch in freqs:
                freqs[ch] += 1
            else:
                freqs[ch] = 1
        total = 0
        pivot = 0
        for _, n in freqs.items():
            total += 2 * (n // 2)
            if (n  % 2):
                pivot = 1
        return total + pivot
