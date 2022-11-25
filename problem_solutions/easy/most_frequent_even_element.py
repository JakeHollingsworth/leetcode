'''
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.
'''
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums:
            if not n % 2:
                counts[n]+= 1
        if not counts:
            return -1
        max_count = max(counts.values())
        return min(n for n,v in counts.items() if v == max_count)
