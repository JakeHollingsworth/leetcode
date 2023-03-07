'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        nums = nums[:-1][::-1]
        min_jumps = []
        if not nums:
            return 0
        for i, n in enumerate(nums):
            if i-n<0:
                min_jumps.append(1)
            elif n == 0:
                min_jumps.append(float('inf'))
            else:
                min_jumps.append(min(min_jumps[max(i-n,0):]) + 1)
        return min_jumps[-1]
