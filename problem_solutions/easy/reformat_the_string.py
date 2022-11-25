'''
You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
'''
class Solution:
    def reformat(self, s: str) -> str:
        a = []
        b = []
        for c in s:
            if c in "0123456789":
                a.append(c)
            else:
                b.append(c)
        a, b = (a,b) if len(a) < len(b) else (b,a)
        if len(b) - len(a) > 1:
            return ''
        else:
            c = b.pop(0) if len(b) - len(a) else ''
            paired = a + b
            paired[::2] = a
            paired[1::2] = b
            return c + ''.join(paired)
