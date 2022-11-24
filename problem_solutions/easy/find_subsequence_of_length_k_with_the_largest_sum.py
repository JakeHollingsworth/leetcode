'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        q = [(-n, i) for i,n in enumerate(nums)]
        heapq.heapify(q)
        res_inds = []
        for _ in range(k):
            _, i = heapq.heappop(q)
            res_inds.append(i)
        return [nums[i] for i in sorted(res_inds)]
