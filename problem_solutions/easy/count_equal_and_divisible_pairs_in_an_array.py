'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
'''
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        loc_dict = defaultdict(list)
        res = 0
        for i, n in enumerate(nums):
            loc_dict[n].append(i)
        for inds in loc_dict.values():
            for start, i in enumerate(inds):
                for j in inds[start+1:]:
                    if not ((i * j) % k):
                        res += 1
        return res
