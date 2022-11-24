'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        return [i+1 for i, n in enumerate(nums) if n > 0]
