'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
'''
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        min_count = len(arr) // 4 + 1
        i = 1
        curr_count = 1
        curr = arr[0]
        while i < len(arr):
            if curr_count >= min_count and arr[i] != curr:
                return curr
            elif arr[i] == curr:
                curr_count += 1
            else:
                curr = arr[i]
                curr_count = 1
            i+= 1
        return curr
