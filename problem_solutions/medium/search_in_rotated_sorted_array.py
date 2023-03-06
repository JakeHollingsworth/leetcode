'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find k, how many rotations occurred in list
        left, right = 0, len(nums) - 1
        k=-1
        while nums[left] > nums[right]:
            k = left + (right - left) // 2
            if nums[k] > nums[left]:
                left = k
            else:
                right = k
        # map between index in hypothetical sorted nums to actual indices in nums.
        map_ind = lambda i: (k + 1 + i) % len(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            med = left + (right - left) // 2
            el = nums[map_ind(med)]
            if el == target:
                return map_ind(med)
            elif el < target:
                left = med + 1
            else:
                right = med
        return map_ind(right) if target == nums[map_ind(right)] else -1
