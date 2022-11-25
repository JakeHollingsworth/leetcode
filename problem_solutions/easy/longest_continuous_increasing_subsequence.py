'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
'''
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        right = 1
        maxlen = 1
        while right < len(nums):
            while right < len(nums) and nums[right] > nums[right-1]:
                right += 1
            maxlen = max(maxlen, right-left)
            left = right
            right += 1
        return maxlen
