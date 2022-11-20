'''
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.

Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

Return true if s is a well-spaced string, otherwise return false.
'''
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i,c in enumerate('abcdefghijklmnopqrstuvwxyz'):
                if c in s and (s.find(c) + distance[i] + 1 >= len(s) or s[s.find(c) + distance[i] + 1] != c):
                    return False
        return True
