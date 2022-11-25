'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sort = sorted(nums)
        indices = {}
        for i, n in enumerate(nums_sort):
            if n not in indices:
                indices[n] = i
        return [indices[n] for n in nums]
