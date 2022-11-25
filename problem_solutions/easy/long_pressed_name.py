'''
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_stack = [c for c in name]
        typed_stack = [c for c in typed]
        while name_stack:
            name_top = name_stack.pop(0)
            typed_top = typed_stack.pop(0)
            if name_top != typed_top:
                return False
            while typed_stack and typed_top == typed_stack[0] and \
                  (not name_stack or name_top != name_stack[0]):
                typed_stack.pop(0)
            if name_stack and not typed_stack:
                return False
        return not typed_stack
            
