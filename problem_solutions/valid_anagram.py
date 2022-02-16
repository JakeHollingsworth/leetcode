'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letts = 26 * [0]
        t_letts = 26 * [0]
        for char1, char2 in zip(s,t):
            s_letts[ord(char1) - 97] += 1
            t_letts[ord(char2) - 97] += 1
        for i, j in zip(s_letts, t_letts):
            if i != j:
                return False
        return True
