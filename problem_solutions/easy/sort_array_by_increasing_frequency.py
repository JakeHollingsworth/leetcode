'''
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = {n:0 for n in nums}
        for n in nums:
            freq_dict[n] += 1
        return sorted(nums, key= lambda x: (freq_dict[x], -x))
