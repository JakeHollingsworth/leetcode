'''
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.
'''
class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        power = 1
        for i, c in enumerate(s[1:]):
            if c == s[i]:
                power += 1
                max_power = max(max_power, power)
            else:
                power = 1
        return max_power
