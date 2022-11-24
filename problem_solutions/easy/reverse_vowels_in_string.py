'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = [ch for ch in s]
        while start < end:
            while start < len(s) and s[start] not in vowels:
                start += 1
            while end >= 0 and s[end] not in vowels:
                end -= 1
            if start < end:
                s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)
