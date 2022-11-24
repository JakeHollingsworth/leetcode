'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
        increasing = nums[-1] - nums[0] >= 0
        return all([d >= 0 for d in diffs]) if increasing else all([d<=0 for d in diffs])
