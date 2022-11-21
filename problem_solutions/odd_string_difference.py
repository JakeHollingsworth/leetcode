'''
You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.
'''
class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = [[ord(c2) - ord(c1) for c1, c2 in zip(w[:-1], w[1:])] for w in words]
        diffs_ans = diffs[0]
        if diffs_ans != diffs[1] and diffs_ans != diffs[2]:
            return words[0]
        else:
            for i, w in enumerate(words):
                if diffs[i] != diffs_ans:
                    return w
        return None
