'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    '''
    We can solve this in O(1) memory by reading forward when we reach a duplicated element until we find a unique number.
    The time complexity is O(N), as running_index runs over all elements of nums exactly once.
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        running_index = 1
        next_unique = 1
        while running_index < len(nums):
            # Read forward at duplicate.
            while running_index < len(nums) and nums[next_unique - 1] == nums[running_index]:
                running_index += 1
            if running_index < len(nums):
                nums[next_unique] = nums[running_index]
                next_unique += 1
                running_index += 1
        return next_unique
            
