'''
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        count = 0
        for n in nums:
            count += nums_dict[n-k] if (n-k) in nums_dict else 0
            count += nums_dict[n+k] if (n+k) in nums_dict else 0
            if n not in nums_dict:
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1
        return count

