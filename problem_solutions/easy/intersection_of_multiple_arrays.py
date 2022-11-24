'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
'''
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums_count = Counter([item for sublist in nums for item in sublist])
        return sorted(n for n,c in nums_count.items() if c == len(nums))
