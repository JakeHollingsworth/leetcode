'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
'''
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freqs = {}
        for n in nums:
            if n in freqs:
                freqs[n] += 1
            else:
                freqs[n] = 1
        return sum([n for n, count in freqs.items() if count == 1])
