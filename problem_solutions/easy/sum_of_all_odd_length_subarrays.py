'''
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        num_counts = [((i+1) * (len(arr) - i) + 1) // 2 for i in range(len(arr))]
        return sum([n * c for n, c in zip(arr, num_counts)]) 
