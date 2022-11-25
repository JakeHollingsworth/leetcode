'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        while len(nums)>2:
            if sum(nums[1:3]) > nums[0]:
                return sum(nums[:3])
            else:
                nums.pop(0)
        return 0
