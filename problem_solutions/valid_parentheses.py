'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    '''
    This is a canonical problem illustrating the utility of stacks. The solution is trivial with the correct data structure: simply pop
    if the character is complementary to the char at the top of the stack. O(N) time complexity.
    '''
    def isValid(self, s: str) -> bool:
        complementary_chars = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char not in complementary_chars:
                stack.append(char)
            else:
                if stack and stack[-1] == complementary_chars[char]:
                    stack.pop()
                else:
                    return False
        return not stack
