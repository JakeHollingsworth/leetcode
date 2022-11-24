'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_balanced = 0
        nL = 0
        nR = 0
        for c in s:
            if c == 'L':
                nL += 1
            if c == 'R':
                nR += 1
            if not (nL - nR):
                num_balanced += 1
                nL = 0
                nR = 0
        return num_balanced
