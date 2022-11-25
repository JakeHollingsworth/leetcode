'''
You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.
'''
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        dedupe = []
        for n in nums:
            if not dedupe or (dedupe and n != dedupe[-1]):
                dedupe.append(n)
        return sum(((dedupe[i-1] - dedupe[i]) * (dedupe[i+1] - dedupe[i])) > 0 for i in range(1, len(dedupe)-1))
