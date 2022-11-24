'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
'''
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = -1
        for n in nums[1:]:
            if n <= curr_min:
                curr_min = n
            elif n - curr_min > curr_max:
                curr_max = n - curr_min
        return curr_max
