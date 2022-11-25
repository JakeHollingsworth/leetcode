'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

class Solution:
    '''
    Boyer Moore majority vote
    '''
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        num_cand = 0
        for n in nums:
            if num_cand == 0:
                cand = n 
            num_cand += (1 if n==cand else -1)
        return cand
