'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
'''
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def strtodict(s):
            d = {}
            for w in s.split(" "):
                if w in d:
                    d[w] += 1
                else:
                    d[w] = 1
            return d
        d1 = strtodict(s1)
        d2 = strtodict(s2)
        uncommon_words = [w for w,c in d1.items() if w not in d2 and c < 2]
        uncommon_words += [w for w, c in d2.items() if w not in d1 and c < 2]
        return uncommon_words
