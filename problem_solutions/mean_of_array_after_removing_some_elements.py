'''
Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.
'''
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        num_to_trim = len(arr) // 20
        arr.sort()
        return sum(arr[num_to_trim:-num_to_trim]) / (len(arr) - 2 * num_to_trim)
