'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = {}
        for c in s:
            counter[c] = counter[c] + 1 if c in counter else 1
        return all([count == counter[s[0]] for _, count in counter.items()])
