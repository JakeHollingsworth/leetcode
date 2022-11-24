'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts_dict = {}
        arr2_set = set(arr2)
        for n in arr1:
            if n in counts_dict:
                counts_dict[n] += 1
            else:
                counts_dict[n] = 1
        result = []
        for n in arr2:
            result += [n for _ in range(counts_dict[n])]
        left = [n for n in arr1 if n not in arr2_set]
        left.sort()
        result += left
        return result
