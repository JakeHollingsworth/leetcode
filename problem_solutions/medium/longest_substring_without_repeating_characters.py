'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
'''
class Solution:
    def maximally_extend_window(self, start, end, s, char_set):
        while end < len(s) and s[end] not in char_set:
            char_set.add(s[end])
            end += 1
        return end
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        char_set = {s[0]}
        start = 0 
        end = 1
        max_len = 1
        while end < len(s):
            end = self.maximally_extend_window(start, end, s, char_set)
            max_len = max(end-start, max_len)
            char_set.remove(s[start])
            start += 1
        return max_len
