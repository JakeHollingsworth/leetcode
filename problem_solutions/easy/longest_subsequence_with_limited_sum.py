'''
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def bin_search(q, sums, left, right):
            mid = left + (right - left) // 2
            if (right - left) <= 1:
                return left
            elif q < sums[mid]:
                return bin_search(q, sums, left, mid) 
            else:
                return bin_search(q, sums, mid, right)        
        nums.sort()
        cumulative_sum = [0]
        for n in nums:
            cumulative_sum.append(n + cumulative_sum[-1])
        res = []
        return [bin_search(q, cumulative_sum, 0, len(cumulative_sum)) for q in queries]
