'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < len(nums) and not nums[left] % 2:
                left += 1
            while right >= 0 and nums[right] % 2:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return nums
