'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if s.count(c) > 1:
                    return True
            else:
                return False
        diffs = 0
        first = ''
        for c, g in zip(s,goal):
            if c != g:
                if not diffs:
                    first_g = g
                    first_s = c
                    diffs += 1
                elif diffs == 1 and first_g == c and first_s == g:
                    diffs += 1
                else:
                    return False
        return diffs == 2
