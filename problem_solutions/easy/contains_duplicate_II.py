'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contained_nums = set(nums[:k+1])
        if len(contained_nums) != len(nums[:k+1]):
            return True
        for i in range(k+1, len(nums)):
            contained_nums.remove(nums[i-(k+1)])
            if nums[i] in contained_nums:
                return True
            contained_nums.add(nums[i])
        return False
