'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split(' ')])
