'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        max_len = 0
        for n, c in counts.items():
            if n+1 in counts:
                max_len = max(max_len, c + counts[n+1])
        return max_len
