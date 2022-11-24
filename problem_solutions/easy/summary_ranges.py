'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i=0
        is_interval = False
        while i < len(nums):
            rnge = str(nums[i])
            while i+1 < len(nums) and nums[i+1] == nums[i] + 1:
                is_interval = True
                i += 1
            if is_interval:
                rnge += "->" + str(nums[i])
                is_interval = False
            i += 1
            ranges.append(rnge)
        return ranges
