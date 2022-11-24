'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        max_val = max(nums)
        nums.remove(max_val)
        if nums:
            nums.remove(max(nums))
        else:
            return max_val
        return max(nums) if nums else max_val
