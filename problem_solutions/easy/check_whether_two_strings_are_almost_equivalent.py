'''
Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.
'''
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        frequency_dict = {}
        for c in word1:
            if c in frequency_dict:
                frequency_dict[c][0] += 1
            else:
                frequency_dict[c] = [1,0]
        for c in word2:
            if c in frequency_dict:
                frequency_dict[c][1] += 1
            else:
                frequency_dict[c] = [0,1]
        return all(abs(c1-c2) <= 3 for c1, c2 in frequency_dict.values())
