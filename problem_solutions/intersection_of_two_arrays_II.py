'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}        
        for n in nums1:
            if n in nums1_dict:
                nums1_dict[n] += 1
            else:
                nums1_dict[n] = 1
        nums2_dict = {}
        for n in nums2:
            if n in nums2_dict:
                nums2_dict[n] += 1
            else:
                nums2_dict[n] = 1
        result = []
        for n in nums1_dict.keys():
            if n in nums1_dict and n in nums2_dict:
                result += min(nums1_dict[n], nums2_dict[n]) * [n]
        return result
