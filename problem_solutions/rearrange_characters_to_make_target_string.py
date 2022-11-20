'''
You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.

Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
'''
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        t_counts = Counter(target)
        return min(s_counts[c] // t_counts[c] for c in t_counts.keys())
