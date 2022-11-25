'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',\
                   'p','q','r','s','t','u','v','w','x','y','z', '0','1','2','3',\
                   '4', '5','6','7','8','9'}
        s = s.lower()
        cleaned = []
        for char in s:
            if char in allowed:
                cleaned.append(char)
        cleaned = "".join(cleaned)
        return cleaned == cleaned[::-1]
