'''
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.
'''
class Solution:
    def equalFrequency(self, word: str) -> bool:
        word_dict = Counter(word)
        unique_frequencies = Counter(word_dict.values())
        keys = list(unique_frequencies.keys())
        vals = list(unique_frequencies.values())
        print(keys, vals)
        if len(keys) == 1:
            return 1 in vals or 1 in keys # 1 letter repeated n times or n letters repeated once
        if len(keys) == 2:
            if 1 in keys and unique_frequencies[1] == 1:
                return True            
            if abs(keys[0] - keys[1]) == 1 and unique_frequencies[max(keys)] == 1:
                return True
        return False
