'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_counts = {}
        for n in nums:
            nums_counts[n] = 1 if n not in nums_counts else nums_counts[n] + 1
        return sum([count * (count-1) // 2 for _, count in nums_counts.items()])     
