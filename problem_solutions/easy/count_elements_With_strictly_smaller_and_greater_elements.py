'''
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.
'''
class Solution:
    def countElements(self, nums: List[int]) -> int:
        mini, maxi = min(nums), max(nums)
        return len([n for n in nums if n != mini and n != maxi])
