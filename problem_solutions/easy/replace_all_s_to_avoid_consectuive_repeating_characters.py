'''
Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
'''
class Solution:
    def modifyString(self, s: str) -> str:
        s_list = [c for c in s]
        swaps = ['a', 'b', 'c']
        for i, c in enumerate(s_list):
            if c == '?':
                for sw in swaps:
                    if (i == 0 or s_list[i-1] != sw) and (i == len(s_list)-1 or s_list[i+1] != sw):
                        s_list[i] = sw
        return "".join(s_list)
