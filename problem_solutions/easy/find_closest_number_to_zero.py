'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
'''
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_abs = min(abs(m) for m in nums)
        return max(n for n in nums if abs(n) == min_abs)
