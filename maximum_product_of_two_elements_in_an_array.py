'''
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1_i = nums.index(max(nums))
        ni = nums.pop(max1_i)
        nj = max(nums)
        return (ni - 1) * (nj - 1)
