'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr_stepsize = (max(arr) - min(arr)) / (len(arr) - 1)
        if arr_stepsize == 0:
            return True
        if arr_stepsize != int(arr_stepsize):
            return False
        arr_stepsize = int(arr_stepsize)
        arr_set = set(arr)
        for k in range(min(arr) + arr_stepsize, max(arr), arr_stepsize):
            if k not in arr_set:
                return False
        return True
