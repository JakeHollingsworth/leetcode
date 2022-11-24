'''
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e = 0
        o = 1
        while e < len(nums) and o < len(nums):
            while e < len(nums) and not nums[e] % 2:
                e += 2
            while o < len(nums) and nums[o] % 2:
                o += 2
            if e < len(nums) and o < len(nums):
                nums[e], nums[o] = nums[o], nums[e]
                e += 2
                o += 2
        return nums
