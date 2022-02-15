'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        This is a canonical binary search problem. The computational complexity of binary search is O(log N). Here we will implement
        the iterative implementation, which has space complexity O(1)
        '''
        start = 0
        end = len(nums)
        while start < end:
            med = start + (end - start) // 2
            if nums[med] == target:
                return med
            elif nums[med] > target:
                end = med
            else:
                start = med + 1
        return start
           
    		
