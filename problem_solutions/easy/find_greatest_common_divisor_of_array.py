'''
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini, maxi = min(nums), max(nums)
        while mini:
            mini, maxi = maxi % mini, mini
        return maxi
