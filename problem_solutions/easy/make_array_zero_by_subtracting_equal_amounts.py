'''
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        curr_sub = 0
        curr_ops = 0
        for n in nums:
            if n > curr_sub:
                curr_ops += 1
                curr_sub += n - curr_sub
        return curr_ops
