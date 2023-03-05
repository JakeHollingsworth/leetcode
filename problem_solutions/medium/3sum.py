'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(lst, target):
            dct = Counter(lst)
            for n in dct:
                if target - n in dct:
                    if target-n != n or dct[n] > 1:
                        yield tuple(sorted([n, target-n, -target]))

        dedupes = set([])
        for i,n in enumerate(nums):
            lst = nums[:i] + (nums[i+1:] if i + 1 < len(nums) else [])
            for x in two_sum(lst, -n):
                dedupes.add(x)
        return map(list, dedupes)
