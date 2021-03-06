'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        # Two loops for O(1) space
        for ch in s:
            result^=ord(ch)
        for ch in t:
            result^=ord(ch)
        return chr(result)
