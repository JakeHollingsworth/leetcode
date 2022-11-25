'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        range_set = set([])
        s_rebuilt = []
        for i, char in enumerate(s):
            if s[i] not in char_map:
                if t[i] in range_set:
                    return False
                char_map[s[i]] = t[i]
                range_set.add(t[i])
            s_rebuilt += [char_map[s[i]]]
        return "".join(s_rebuilt) == t
