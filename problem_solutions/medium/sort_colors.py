'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort
        rwb = [0,0,0]
        for n in nums:
            rwb[n] += 1
        curr = 0
        for i in range(len(nums)):
            while not rwb[curr]:
                curr += 1
            nums[i] = curr
            rwb[curr] -= 1    
