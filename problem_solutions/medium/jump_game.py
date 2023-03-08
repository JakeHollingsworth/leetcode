'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = []
        nums = nums[:-1][::-1]
        for i, n in enumerate(nums):
            if n > i:
                ans.append(True)
            elif not n:
                ans.append(False)
            else:
                ans.append(any(ans[max(i-n, 0):]))
        return True if not ans else ans[-1]
