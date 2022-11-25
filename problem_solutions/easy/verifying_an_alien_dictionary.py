'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorter = lambda x: tuple([order.index(c) for c in x])
        return words == sorted(words, key=sorter)
