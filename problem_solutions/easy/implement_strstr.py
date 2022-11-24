'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    '''
    We perform a sliding window search for needle in haystack. The window is a fixed size of len(needle). The complexity is O(N), but see
    readme on string splicing.
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack == needle: return 0
        for i, j in zip(range(len(haystack) - len(needle)+1), range(len(needle), len(haystack)+1)):
            if haystack[i:j] == needle: return i
        return -1
        
