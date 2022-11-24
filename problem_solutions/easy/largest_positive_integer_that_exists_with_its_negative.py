'''
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
'''
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        candidates = [k for k in nums if -k in nums]
        return max(candidates) if candidates else -1
