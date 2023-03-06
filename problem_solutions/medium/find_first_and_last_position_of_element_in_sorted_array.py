'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # Find left-most target
        left = 0
        right = len(nums) - 1
        while left < right:
            med = left + (right - left) // 2
            if nums[med] < target:
                left = med + 1
            else:
                right = med
        left_ind = left
        # Find right-most target
        left = 0
        right = len(nums) - 1
        while left < right:
            med = left + (right - left) // 2
            print(left, med, right)
            if nums[med] <= target:
                left = med+1
            else:
                right = med
        right_ind = right
        if left_ind < len(nums) and nums[left_ind] != target and nums[right_ind] != target:
            return [-1, -1]
        else:
            return [left_ind, right_ind -1 + (1 if nums[right_ind] == target else 0)]
