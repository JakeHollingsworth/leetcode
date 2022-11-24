'''
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.
'''
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        for i, n in enumerate(nums):
            if i == 0 or n > nums[i-1]:
                curr_sum += n
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = n
        return max_sum
