'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        nums *= 2
        num_no_decreases = 0
        for a, b in zip(nums[:-1], nums[1:]):
            if b - a >= 0:
                num_no_decreases += 1
            else:
                num_no_decreases = 0
            if num_no_decreases == n-1:
                return True
        return n == 1
