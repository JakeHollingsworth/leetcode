'''
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
            else:
                curr.append(nums[i])
                dfs(i+1)

                curr.pop()
                dfs(i+1)
        dfs(0)
        return res
