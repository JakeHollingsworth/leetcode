'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        mins = [nums[0], nums[1]]
        maxs = [nums[0], nums[1], nums[2]]
        mins.sort()
        maxs.sort()
        for i, n in enumerate(nums[2:]):
            if i != 0 and n > maxs[0]:
                maxs[0] = n
                maxs.sort()
            if n < mins[-1]:
                mins[-1] = n
                mins.sort()
        return max(mins[0] * mins[1] * maxs[2], maxs[0] * maxs[1] * maxs[2])
        
