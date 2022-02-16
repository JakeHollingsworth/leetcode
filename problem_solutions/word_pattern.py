'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split(' ')
        if len(pattern) != len(s_split):
            return False
        char_map = {}
        word_map = set([])
        candidate_match = []
        for char, word in zip(pattern, s_split):
            if char not in char_map:
                if word in word_map:
                    return False
                word_map.add(word)
                char_map[char] = word
            candidate_match.append(char_map[char])
        if ' '.join(candidate_match) == ' '.join(s_split):
            return True
        return False
