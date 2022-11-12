'''
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
'''
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def binary_search(n, arr2):
            left = 0
            right = len(arr2)
            while left < right:
                med = left + (right - left) // 2
                if left + 1 == right or n == arr2[med]:
                    return med
                elif n < arr2[med]:
                    right = med
                else:
                    left = med + 1
            return left
        arr2.sort()
        total = 0
        for n in arr1:
            n_ind = binary_search(n, arr2)
            if (n_ind - 1 < 0 or abs(n - arr2[n_ind - 1]) > d) and \
               (n_ind == len(arr2) or abs(n - arr2[n_ind]) > d) and \
               (n_ind+1 >= len(arr2) or abs(n - arr2[n_ind+1]) > d):
                total += 1
        return total
