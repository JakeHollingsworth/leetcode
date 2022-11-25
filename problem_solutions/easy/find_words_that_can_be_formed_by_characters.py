'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = {}
        num_w = 0
        for c in chars:
            chars_dict[c] = chars_dict[c] + 1 if c in chars_dict else 1
        for w in words:
            curr_dict = chars_dict.copy()
            contained = len(w)
            for c in w:
                if c not in curr_dict or not curr_dict[c]:
                    contained = 0
                else:
                    curr_dict[c] -= 1
            num_w += contained
        return num_w
