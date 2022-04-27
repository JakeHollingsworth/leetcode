'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
'''
class Solution:
    def maxScore(self, s: str) -> int:
        score = (1 if s[0] == '0' else 0) + s[1:].count('1')
        max_score = score
        for i in range(1, len(s)-1):
            score += 1 if s[i] == '0' else -1
            max_score = max(max_score, score)
        return max_score
