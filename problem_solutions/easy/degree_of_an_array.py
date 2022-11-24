'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        degree = max([d for _, d in counts.items()])
        subarr_lens = []
        for n in counts:
            if counts[n] == degree:
                first = 0
                last = len(nums) - 1
                while nums[first] != n:
                    first += 1
                while nums[last] != n:
                    last -= 1
                subarr_lens.append(last-first+1)
        return min(subarr_lens)
