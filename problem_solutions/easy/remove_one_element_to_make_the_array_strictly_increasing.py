'''
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
'''
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check_monotonic_increase(x):
            for i in range(1, len(x)):
                if x[i-1] >= x[i]:
                    return False
            return True
        if check_monotonic_increase(nums):
            return True
        extrema = []
        for i in range(len(nums)):
            if i == 0 or nums[i] <= nums[i-1] or i == len(nums) -1 or nums[i] >= nums[i+1]:
                extrema += [i]    
        for i in extrema:
            if check_monotonic_increase(nums[:i] + (nums[i+1:] if i != len(nums) else [])):
                return True
        return False
