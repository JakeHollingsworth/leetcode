'''
You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

0 <= i <= nums.length - 2,
nums[i] == key and,
nums[i + 1] == target.
Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.
'''
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets = []
        for i, n in enumerate(nums[:-1]):
            if n == key:
                targets.append(nums[i+1])
        freqs = Counter(targets)
        curr_max = -1
        target = -1
        for n, f in freqs.items():
            if f > curr_max:
                target = n
                curr_max = f 
        return target
