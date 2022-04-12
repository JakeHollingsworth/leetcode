'''
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.
'''
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        tot = 0
        last_added = 0
        while k > 0:
            if not nums:
                return tot - 2 * last_added * (k % 2)
            elif abs(nums[0]) >= abs(nums[-1]):
                n = nums.pop(0)
                if n < 0:
                    last_added = -n
                    k -= 1
                else:
                    last_added = n
            else:
                last_added = nums.pop(-1)
            tot += last_added
        return tot + sum(nums)
