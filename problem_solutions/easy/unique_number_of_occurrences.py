'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts_dict = {}
        for n in arr:
            num_counts = arr.count(n)
            if num_counts in counts_dict and counts_dict[num_counts] != n:
                return False
            else:
                counts_dict[num_counts] = n
        return True
