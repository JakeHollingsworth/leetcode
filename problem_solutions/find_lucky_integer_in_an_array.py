'''
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
'''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        for n in arr:
            counts[n] = counts[n] + 1 if n in counts else 1
        lucky_nums = [n for n, c in counts.items() if n == c]
        return max(lucky_nums) if lucky_nums else -1
