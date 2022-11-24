'''
You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.
'''
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counts = Counter(nums)
        left = 0
        right = len(nums)
        res = 0
        for f in counts.values():
            right -= f
            res += left * f * right
            left += f 
        return res
