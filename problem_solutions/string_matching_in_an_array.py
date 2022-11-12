'''
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key = lambda x: len(x))
        return [w for i, w in enumerate(words) if any([w in x for x in words[i+1:]])]
