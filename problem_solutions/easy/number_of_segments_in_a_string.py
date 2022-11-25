'''
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.
'''
class Solution:
    def countSegments(self, s: str) -> int:
        splits = s.strip().split(' ')
        splits = [sp for sp in splits if sp != '']
        return len(splits) if s else 0
