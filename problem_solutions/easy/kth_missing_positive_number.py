'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0 
        right = len(arr)
        while left < right:
            med = left + (right - left) // 2
            if arr[med] - med - 1 < k:
                left = med + 1
            else:
                right = med
        return left + k
