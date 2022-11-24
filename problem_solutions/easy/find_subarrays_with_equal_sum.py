'''
Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.
'''
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums_set = set([])
        for n,m in zip(nums, nums[1:]):
            if n + m in sums_set:
                return True
            else:
                sums_set.add(n+m)
        return False
