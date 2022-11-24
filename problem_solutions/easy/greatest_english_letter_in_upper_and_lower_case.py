'''
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.
'''
class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabet ='abcdefghijklmnopqrstuvwxyz'
        max_c = ''
        for c in alphabet:
            if c in s and c.upper() in s:
                max_c = c.upper()
        return max_c
