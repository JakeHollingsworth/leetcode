'''
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
'''
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        subseq = []
        nums.sort()
        total_subseq = 0
        total_nums = sum(nums)
        while total_subseq <= total_nums and nums:
            el = nums.pop(-1)
            total_subseq += el
            total_nums -= el
            subseq.append(el)
        return subseq
