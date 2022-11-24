'''
You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".


'''
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        word_counts = [Counter(w) for w in words]
        for i in range(1, len(words)):
            if word_counts[i-1] != word_counts[i]:
                res.append(words[i])
        return res
