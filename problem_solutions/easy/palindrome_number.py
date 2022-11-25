'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
'''

class Solution:
    '''
    We can simply calculate x_reversed = (x with reversed digits) and check x == x_reversed
    '''
    def isPalindrome(self, x: int) -> bool:
        x_original = x
        x_reversed = 0
        while x > 0:
            x_reversed = x_reversed * 10 + x % 10
            x //= 10
        return x_original == x_reversed
