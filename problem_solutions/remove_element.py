'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    '''
    Swap elements to delete to the end of the array. O(N) solution.
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        num_value = 0
        i = 0
        while i < len(nums) - num_value:
            while nums[i] == val and num_value < len(nums)  and i < len(nums) - num_value:
                num_value += 1
                nums[i], nums[-num_value] = nums[-num_value], nums[i]
            i += 1
        return len(nums) - num_value
                 
