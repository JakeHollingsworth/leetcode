'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        for i in range(len(arr)-1, -1, -1):
            next_max = max(curr_max, arr[i])
            arr[i] = curr_max
            curr_max = next_max
        return arr
