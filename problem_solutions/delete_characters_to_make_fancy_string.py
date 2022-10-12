'''
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.
'''
class Solution:
    def makeFancyString(self, s: str) -> str:
        w = []
        for c in s:
            if len(w) < 2 or not (c == w[-1] and c == w[-2]):
                w.append(c)
        return ''.join(w)
