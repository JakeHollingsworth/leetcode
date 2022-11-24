'''
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
        rank_dict = {n: i+1 for i,n in enumerate(sorted_arr)}
        for i, n in enumerate(arr):
            arr[i] = rank_dict[n]
        return arr
