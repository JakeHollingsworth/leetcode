'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
'''
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        results = []
        counts = {w:{c:w.count(c) for c in w} for w in words}
        shortest = min(words, key=len)
        for c, _ in counts[shortest].items():
            while all([c in chars and chars[c] > 0 for _, chars in counts.items()]):
                results.append(c)
                for _, chars in counts.items():
                    chars[c] -= 1
        return results
