'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        while nums:
            if abs(nums[0]) < abs(nums[-1]):
                result.append(nums.pop(-1) ** 2)
            else:
                result.append(nums.pop(0) ** 2)
        return result[::-1]
