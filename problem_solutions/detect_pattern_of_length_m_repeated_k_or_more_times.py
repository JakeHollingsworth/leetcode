'''
Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
'''
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        repeats_length = 0
        for a,b in zip(arr[:-m], arr[m:]):
            if a != b:
                repeats_length = 0
            else:
                repeats_length += 1
            if repeats_length == (k-1) * m:
                return True
        return False
