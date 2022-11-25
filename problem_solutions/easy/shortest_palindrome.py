'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        stack = []
        # Find palindromic prefix
        prefix_length = 0
        for i in range(len(s)+1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                prefix_length = i
        return s[::-1][:-prefix_length] + s
