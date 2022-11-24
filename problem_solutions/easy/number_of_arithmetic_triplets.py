'''
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.
'''
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        diff_set = set(nums)
        res = 0
        for n in nums:
            if n+diff in diff_set and n + 2*diff in diff_set:
                res += 1
        return res
