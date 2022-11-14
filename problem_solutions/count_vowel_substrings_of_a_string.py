'''
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.
'''
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels='aeiou'
        most_recent_consonant = -1
        most_recent_vowel={v:-1 for v in vowels}
        res = 0
        for i, c in enumerate(word):
            if c not in vowels:
                most_recent_consonant = i 
            else:
                most_recent_vowel[c] = i
            res += max(min(most_recent_vowel.values()), most_recent_consonant) - most_recent_consonant
        return res
