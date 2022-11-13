'''
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        snums1 = set(nums1)
        snums2 = set(nums2)
        snums3 = set(nums3)
        snums = set(nums1 + nums2 + nums3)
        return [n for n in snums if (n in snums1) + (n in snums2) + (n in snums3) > 1]
