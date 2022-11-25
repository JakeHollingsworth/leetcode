'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_stack(r):
            r_stack = []
            for c in r:
                if c == '#':
                    if r_stack:
                        r_stack.pop(-1)
                else:
                    r_stack.append(c)
            return "".join(r_stack)
        return build_stack(s) == build_stack(t)
