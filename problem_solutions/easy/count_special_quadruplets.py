'''
Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d
'''
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        for i, x in enumerate(nums[:-2]):
            for j, y in enumerate(nums[i+1:-1]):
                for k, z in enumerate(nums[i+j+2:]):
                    if (x + y + z in nums[i+j+k+2:]):
                        res += nums[i+j+k+2:].count(x+y+z)
        return res
