'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            return [[n] + x for i, n in enumerate(nums) for x in self.permute(nums[0:i] + nums[i+1:])]
