'''
You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
'''
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        inds = []
        for i, n in enumerate(nums):
            if n == key:
                for j in range(max(inds[-1]+1 if inds else 0, i-k), min(i+k+1, len(nums))):
                    inds.append(j)
        return inds
