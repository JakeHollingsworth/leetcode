'''
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
'''
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        candidates = [n for n in nums if not (n % 6)]
        return sum(candidates) // len(candidates) if candidates else 0
