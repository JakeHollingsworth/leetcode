'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i < len(arr):
            n = arr[i]
            if not n:
                arr.insert(i+1, 0)
                arr.pop()
                i += 2
            else:
                i+=1
        return arr
