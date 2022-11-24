'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                nums[i] = nums[i-1] + 1 if i > 0 else 1
            else:
                nums[i] = 0
            i += 1
        return max(nums)
