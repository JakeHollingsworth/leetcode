'''
You are given a string s. Reorder the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
'''
class Solution:
    def sortString(self, s: str) -> str:
        res = []
        char_dict = Counter(s)
        chars = char_dict.keys()
        chars_asc = sorted(chars)
        while len(res) < len(s):
            for c in chars_asc:
                if char_dict[c]:
                    res.append(c)
                    char_dict[c] -= 1
            for c in chars_asc[::-1]:
                if char_dict[c]:
                    res.append(c)
                    char_dict[c] -= 1
        return ''.join(res)

