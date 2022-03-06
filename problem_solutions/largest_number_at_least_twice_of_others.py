'''
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        twice_second_largest = -float('inf')
        largest = 0
        for i, n in enumerate(nums):
            if n > nums[largest]:
                twice_second_largest = 2 * nums[largest]
                largest = i
            elif 2 * n > twice_second_largest and i != 0:
                twice_second_largest = 2 * n
        return largest if nums[largest] >= twice_second_largest else -1
