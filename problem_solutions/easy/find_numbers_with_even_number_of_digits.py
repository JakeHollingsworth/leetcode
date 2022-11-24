'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num_even = 0
        for n in nums:
            even = True
            while n > 0:
                even = not even
                n //= 10
            num_even += 1 if even else 0
        return num_even
