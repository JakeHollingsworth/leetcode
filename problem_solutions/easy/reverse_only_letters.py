'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz' 
        letters += letters.upper()
        left = 0
        right = len(s) - 1
        s = [c for c in s]
        while left < right:
            while left < len(s) and s[left] not in letters:
                left += 1
            while right >= 0 and s[right] not in letters:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
