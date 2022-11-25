'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for ch in s:
            if ch not in counts:
                counts[ch] = s.count(ch)
        s_counts = [counts[ch] for ch in s]
        unique_inds = [i for i,n in enumerate(s_counts) if n == 1]
        return unique_inds[0] if unique_inds else -1
