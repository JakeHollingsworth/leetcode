'''
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.
'''
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        num_words = len(words)
        letter_bank = {}
        for s in words:
            for c in s:
                if c in letter_bank:
                    letter_bank[c] += 1
                else:
                    letter_bank[c] = 1
        for c, count in letter_bank.items():
            if count % num_words:
                return False
        return True
