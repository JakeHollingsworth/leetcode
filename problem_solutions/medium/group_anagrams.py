'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for s in strs:
            list_key = [0 for i in range(26)]
            for c in s:
                list_key[ord(c) - ord('a')] += 1
            key = ' '.join([str(x) for x in list_key])
            if key in anagrams_dict:
                anagrams_dict[key].append(s)
            else:
                anagrams_dict[key] = [s]
        return anagrams_dict.values()
