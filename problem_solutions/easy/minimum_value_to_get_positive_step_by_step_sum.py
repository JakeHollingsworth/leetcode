'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumulative = [nums[0]]
        for n in nums[1:]:
            cumulative.append(cumulative[-1] + n)
        floor = min(cumulative)
        return -floor + 1 if -floor + 1 > 0 else 1
