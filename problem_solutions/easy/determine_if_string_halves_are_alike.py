'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
'''
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.upper()
        vowels = ['A', 'E', 'I', 'O', 'U']
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        return sum([s1.count(v) for v in vowels]) == sum([s2.count(v) for v in vowels])
