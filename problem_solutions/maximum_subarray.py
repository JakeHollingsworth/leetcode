'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''

class Solution:
    '''
    Kadane's algorithm
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] >= 0:
                nums[i] += nums[i-1]
        return max(nums)
