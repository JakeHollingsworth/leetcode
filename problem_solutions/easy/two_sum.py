'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

from typing import List

class Solution:
    '''
    This problem tests the ability to leverage O(1) look ups for dictionaries in python. The optimal solution is O(N), and is 
    achieved by converting nums to a dict. For n in the dict, we can evaluate whether (target - n) is in the set in constant time.
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {n:i for i,n in enumerate(nums)}
        for i,n in enumerate(nums):
            if target-n in nums_dict and i != nums_dict[target-n]:
                return [i, nums_dict[target-n]]
        raise Exception
