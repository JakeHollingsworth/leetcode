'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                left_remove, right_remove = s[i+1:j+1], s[i:j]
                return left_remove == left_remove[::-1] or right_remove == right_remove[::-1]
            i += 1
            j -= 1
        return True if s[::-1] == s else False
