'''
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
'''
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        res = 0
        for w in w1:
            if w1[w] == 1 and w in w2 and w2[w] == 1:
                res += 1
        return res
