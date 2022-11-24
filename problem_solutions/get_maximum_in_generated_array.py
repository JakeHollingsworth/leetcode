'''
You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.
'''
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        for i in range(2, n+1):
            nums.append(nums[i//2] if not i%2 else nums[i// 2] + nums[(i+1) // 2])
        return max(nums[:n+1])
