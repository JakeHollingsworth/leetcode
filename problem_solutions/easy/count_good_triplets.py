'''
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.
'''
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i, x in enumerate(arr[:-2]):
            for j, y in enumerate(arr[i+1:-1]):
                if abs(x-y) <= a:
                    for k, z in enumerate(arr[i+j+2:]):
                        if abs(y-z) <= b and abs(x-z) <= c:
                            count += 1
        return count
