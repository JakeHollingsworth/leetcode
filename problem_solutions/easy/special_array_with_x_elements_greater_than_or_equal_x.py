'''
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
'''
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= len(nums):
            return len(nums)
        for i, n in enumerate(nums[:-1]):
            candidate = len(nums) - i - 1
            if candidate > n and candidate <= nums[i+1]:
                return candidate
        return -1
