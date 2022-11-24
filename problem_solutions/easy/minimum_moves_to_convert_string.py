'''
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.
'''
class Solution:
    def minimumMoves(self, s: str) -> int:
        flips = [(0 if s[:i+1] == (i+1) * 'O' else 1) for i in range(3)]
        for i in range(3, len(s)):
            temp = 1 + flips[-3]
            if s[i] == 'O':
                temp = min(temp, flips[-1])
            flips.append(temp)
        return flips[-1]
