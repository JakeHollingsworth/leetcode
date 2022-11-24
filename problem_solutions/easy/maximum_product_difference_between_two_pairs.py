'''
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
'''
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1, min2, max2, max1 = [i[0] for i in sorted(enumerate(nums[:4]), key=lambda x:x[1])]
        for i, n in enumerate(nums[4:]):
            if n < nums[min2]:
                if n < nums[min1]:
                    min2, min1 = min1, i+4
                else:
                    min2 = i + 4
            elif n > nums[max2]:
                if n > nums[max1]:
                    max2, max1 = max1, i+4
                else:
                    max2 = i + 4
        return nums[max1] * nums[max2] - nums[min1] * nums[min2]
            
